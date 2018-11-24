<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>
<%@include file="/WEB-INF/common/taglibs.jsp"%>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>news</title>
</head>
<body>
  <div class="box">
	<table class="table">
		<thead>
			<tr>
				<th>序号</th>
				<th>数据来源</th>
				<th>网址</th>
				<th>标题</th>
				<th>内容</th>
				<th>发表时间</th>
			</tr>
		</thead>
		<tbody>
			<c:forEach items="${news}" var="newsItem">
				<tr>
					<td>${newsItem.id}</td>					
					<td>${newsItem.data_from}</td>
					<td>${newsItem.url}</td>
					<td>${newsItem.title}</td>
					<td>${newsItem.content}</td>
					<td>${newsItem.time}</td>
				</tr>
			</c:forEach>
		</tbody>
	</table>
  </div>
</body>
</html>