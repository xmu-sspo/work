<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<%-- 当前web应用根目录 --%>
<c:set var="ctx" value="${pageContext.request.contextPath}" />
<%-- js和css文件的路径 --%>
<c:set var="jcPath" value="${pageContext.request.contextPath}" />

<%-- 系统OSS图片路径  
<c:set var="sysImgPath" value="http://ow5q0iqab.bkt.clouddn.com" />
<%-- 系统OSS图片路径  
<c:set var="buyerImgPath" value="http://ow5q0iqab.bkt.clouddn.com" />
<%-- 系统OSS图片路径  -
<c:set var="shopImgPath" value="http://ow5q0iqab.bkt.clouddn.com" />
<%-- 系统OSS图片路径  
<c:set var="sysPicPath" value="http://ow5q0iqab.bkt.clouddn.com" />--%>

<%-- 主工程路径 --%>
<c:set var="mainPath" value="${mainBasePath}" /> 
<%-- <c:set var="sessionUser" value="${sessionScope.buyer}" /> --%>