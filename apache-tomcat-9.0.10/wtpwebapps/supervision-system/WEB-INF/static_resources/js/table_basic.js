/**
 * Created by 朱何莹 on 2018/8/12.
 * 话题列表
 */
var id;
//用window的onload事件，窗体加载完毕的时候
window.onload=function()
{
	//获取从URL中传过来的用户id
	var thisURL = document.URL; 
	if(thisURL.indexOf("?")>=0){
		var getval =thisURL.split('?')[1]; 
		id = getval.split("=")[1]; 
	}
	getUser();
    getTopicList();
}

//获取用户信息
function getUser(){
	if(id){
		$.ajax({
		   url:"/getCurrentUserById",
		   data:{id:id},
		   success:function(data){
			   $("#user_img").attr({title:data.username});
			   $("#user_name_a").html(data.username);
		   },error:function(){
			   alert("获取用户信息失败！");
		   }
	   });
	}
}
	
	

//获取话题列表
function getTopicList(){
	$.ajax({
		   url:"/getTopicList",
		   success:function(data){
			   var topic_list = data;    //话题列表
			   //如果列表为空
			   if(topic_list.length == 0){
				   $("#table_tbody").append("The result is empty.");
				   alert("empty");
			   }else{
				   for(var i=0; i<topic_list.length; i++){
					   var item = topic_list[i];    //其中一个话题
					   var j=i+1;
					   $("#table_tbody").append(
							   "<tr>" 
								+
								"<td>" + j + "</td>"
								+
								"<td>" + "<a style='cursor:pointer' onclick=\"moredetails(\'" + item.news_list +"\')\">" + item.title + "</a>" + "</td>"  
								+
								"<td>" + item.center_index +"</td>"
								+
								"</tr>"	   
					   );
				   }//end for
			   }//end else	   
		   },error:function(){
			   alert("Something about the system went wrong . Please contact the administrator.");
		   }
	   });
}

//查看某个话题中包含的具体新闻
function moredetails(newsList){
	window.location.href="/table_complete?newsList="+newsList;
}