window.onload = function(){
	var thisURL = document.URL; 
	var showval;
	if(thisURL.indexOf("?")>=0){
		var getval =thisURL.split('?')[1]; 
		showval = getval.split("=")[1]; 
	}
	setNews(showval);
}

/** 
 * 时间对象的格式化; 
 */  
Date.prototype.format = function (format)   
{  
    /* 
     * eg:format="YYYY-MM-dd hh:mm:ss"; 
     */  
    var o =   
    {  
        "M+" : this.getMonth() + 1, // month  
        "d+" : this.getDate(), // day  
        "h+" : this.getHours(), // hour  
        "m+" : this.getMinutes(), // minute  
        "s+" : this.getSeconds(), // second  
        "q+" : Math.floor((this.getMonth() + 3)  / 3), // quarter  
        "S" : this.getMilliseconds() // millisecond  
    }  
    if (/(y+)/.test(format))   
    {  
        format = format.replace(RegExp.$1, (this.getFullYear() + "") .substr(4 - RegExp.$1.length));  
    }  
    for ( var k in o)   
    {  
        if (new RegExp("(" + k + ")").test(format))   
        {  
            format = format.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length));  
        }  
    }  
    return format;  
}  

function setNews(id){
	$.ajax({
	url:"/getOneNews",
	data:{id:id},
	success:function(data){
		var news = data;
		var time = new Date(news.time).format('yyyy-MM-dd hh:mm:ss');
		$("#title").html(news.title);
		$("#data_from").html("<label >来源：</label>" + news.data_from);
		$("#url").html("<label >原网址：</label><a href='" + news.url + "' target='_Blank'>" + news.url + "</a>");
		$("#time").html("<label >发表时间：</label>" + time);
//		$("#author").html("<label >作者：</label>" + news.author);
//		$("#browse").html("<label >浏览量：</label>" + news.browse);
//		$("#comment").html("<label >评论数：</label>" + news.comment);
//		$("#clickRate").html("<label >点击量：</label>" + news.click);
		$("#content").html("<label >内容：</label>" + news.content);		
			
	},error:function(){
		alert("Something about the system went wrong . Please contact the administrator.");
	}
});
}