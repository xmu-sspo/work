/**
 * Created by 朱何莹 on 2018/8/31.
 */

var newsList;
var page = 1;
var totalpage;

//用window的onload事件，窗体加载完毕的时候
window.onload=function(){
	var thisURL = document.URL; 
	var showval;
	if(thisURL.indexOf("?")>=0){
		var getval =thisURL.split('?')[1]; 
		showval = getval.split("=");
		if(showval[0]=="newsList")
			setNewsList(showval[1]);
	}
	selectMethod(page);
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

function selectMethod(page){
	if(!newsList)
	{
		loadAllNews(page);
	}
	else
		loadNewsList(page);
}

function setNewsList(newslist){
	newsList = newslist;
}

function loadAllNews(page){
	
	if(page <= 0)
		page = 1;
	
	$.ajax({
		url:"/getAllNews",
		data:{page:(page-1)*15},
		success:function(data){
			var news_list = data.newsList;    //该话题中包含的新闻列表
			totalpage = data.total / 15;
			totalpage = Math.ceil(totalpage);
			//如果返回的列表为空
			if(news_list.length==0){
				 $("#table_tbody").append("The result is empty.");
				 alert("empty");
			}else{
				$("#table_tbody").html("");
				for(var i=0; i<news_list.length; i++){
				   var item = news_list[i];    //其中一个新闻
				   var content;
				   if(item.content.length>50)
					   content = item.content.substring(0,50) + "...";
				   else content = item.content;
				   //时间格式化
				   var time = new Date(item.time).format('yyyy-MM-dd hh:mm:ss');	
				   $("#table_tbody").append(
						   "<tr>" 
							+
							"<td>" + item.id + "</td>"
							+
							"<td>" + "<a onclick='oneNews(" + item.id + ")'>" + item.title + "</a>" + "</td>"
							+
							"<td>" + item.data_from +"</td>"  
							+
							"<td class='am-hide-sm-only'>" + content +"</td>"
							+
							"<td class='am-hide-sm-only'>" + time +"</td>"
							+
							"<td class='am-hide-sm-only'>" + item.click +"</td>"
							+
							"<td class='am-hide-sm-only'>" + "<a href='" + item.url + "' target='_Blank'>...</a>" +"</td>"
							+
							"</tr>"	   
				   );
				}//end for
				
				$("#show_list ul").html("");
				//判断页数以此显示翻页
				if(totalpage > 1)
				{
					var prestr = "<li class='am-disabled'><a href=javascript:pre_page(" + (page - 1) + ")>«</a></li>";
					if(page > 3)
					prestr += "<li><a >...</a></li>";
					$("#show_list ul").append(prestr);
					
					if(page - 2 >= 1)
						$("#show_list ul").append("<li><a href='javascript:loadAllNews( " + (page - 2) + ")'>" + (page - 2) + "</a></li>");		
					if(page - 1 >= 1)
						$("#show_list ul").append("<li><a href='javascript:loadAllNews( " + (page - 1) + ")'>" + (page - 1) + "</a></li>");
					$("#show_list ul").append("<li class='am-active'><a>" + page + "</a></li>");
					if(page < totalpage)
						$("#show_list ul").append("<li><a href='javascript:loadAllNews( " + (page + 1) + ")'>" + (page + 1) + "</a></li>");
					if(page + 1 < totalpage)
						$("#show_list ul").append("<li><a href='javascript:loadAllNews( " + (page + 2) + ")'>" + (page + 2) + "</a></li>");
					
					var nexstr = "<li><a href=javascript:nex_page("+ (page + 1) + ")>»</a></li>";
					if(page < totalpage - 3)
						nexstr = "<li><a >...</a></li>" + nexstr;			
					$("#show_list ul").append(nexstr);
				}//end if(翻页)
				$("#total_records").html("共" + data.total + "条记录");
			}//end else
		},
		error:function(){
			alert("Something about the system went wrong . Please contact the administrator.");
		}
	});
}

function loadNewsList(){	
	$.ajax({
	url:"/getNewsList",
	data:{str:newsList},
	success:function(data){
		var news_list = data;    //该话题中包含的新闻列表
		//如果列表为空
		if(news_list.length==0){
			$("#table_tbody").append("The result is empty.");
			 alert("empty");
		}else{
			$("#table_tbody").html("");
			for(var i=0; i<news_list.length; i++){
			   var item = news_list[i];    //其中一个新闻
			   var content;
			   if(item.content.length>50)
				   content = item.content.substring(0,50) + "...";
			   else content = item.content;
			   //时间格式化
			   var time = new Date(item.time).format('yyyy-MM-dd hh:mm:ss');	
			   $("#table_tbody").append(
					   "<tr>" 
						+
						"<td>" + item.id + "</td>"
						+
						"<td>" + "<a onclick='oneNews(" + item.id + ")'>" + item.title + "</a>" + "</td>"
						+
						"<td>" + item.data_from +"</td>"  
						+
						"<td class='am-hide-sm-only'>" + content +"</td>"
						+
						"<td class='am-hide-sm-only'>" + time +"</td>"
						+
						"<td class='am-hide-sm-only'>" + item.click +"</td>"
						+
						"<td class='am-hide-sm-only'>" + "<a href='" + item.url + "'>...</a>" +"</td>"
						+
						"</tr>"	   
			   );
			}//end for
			$("#total_records").html("共" + data.length + "条记录");
		}//end else
	},error:function(){
		alert("Something about the system went wrong . Please contact the administrator.");
	}
	
});
}

//前一页
function pre_page(page)
{
	selectMethod(page);
}

//后一页
function nex_page(page)
{
	if(page > totalpage)
	{
		page = totalpage
		alert("Not more data.");
	}
	else
		selectMethod(page);
}



//查看具体的一条新闻
function oneNews(id){
	window.location.href="/content?id="+id;
}