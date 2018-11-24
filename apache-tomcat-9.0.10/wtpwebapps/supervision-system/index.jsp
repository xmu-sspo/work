<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>
<%@include file="/WEB-INF/common/taglibs.jsp"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>welcome</title>
	<link rel="stylesheet" type="text/css" href="${ctx }/css/index.css">
</head>
<body>
	<h2>Hello World!</h2>
	<input id="key" name="key" type="text" value=""/>
	<button value="">确定</button><br>
	<p>结果：</p>
	<textarea cols="10" rows="2" id="re-id"></textarea>
	<textarea cols="20" rows="2" id="re-content"></textarea>
	<script>
		var box = document.getElementsByTagName("h2")[0];
		box.onclick = function(){
			console.log("box");
			window.location.href="news"; 
		}
		var keyword = document.getElementById("key"),
			resultId = document.getElementById("re-id"),
			resultContent = document.getElementById("re-content"),
			butt = document.getElementsByTagName("button")[0];
		butt.onclick = function(){
			console.log(keyword.value);
			resultId.innerHTML=keyword.value;
			resultContent.innerHTML=keyword.value;
		}
	</script>
</body>
</html>