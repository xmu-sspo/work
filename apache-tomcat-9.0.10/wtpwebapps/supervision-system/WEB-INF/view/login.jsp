<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>
<%@include file="/WEB-INF/common/taglibs.jsp"%>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>舆情监督系统-用户登录</title>	
		<link rel="stylesheet" href="/css/core.css" />
		<link rel="stylesheet" href="/css/menu.css" />
		<link rel="stylesheet" href="/css/amazeui.css" />
		<link rel="stylesheet" href="/css/component.css" />
		<link rel="stylesheet" href="/css/page/form.css" />
	</head>
	<body >
		<div class="account-pages">
			<div class="wrapper-page">
				<div class="text-center">
	                <a href="/index" class="logo"><span>舆情监督系统</span></a>
	            </div>
	            
	            <div class="m-t-40 card-box">
	            	<div class="text-center">
	                    <h4 class="text-uppercase font-bold m-b-0">用户登录</h4>
	                </div>
	                <div class="panel-body">
	                	<form class="am-form">
	                		<div class="am-g">
	                			<div class="am-form-group">
							      <input id="username" type="text" class="am-radius"  placeholder="用户名">
							    </div>
							
							    <div class="am-form-group form-horizontal m-t-20">
							      <input id="password" type="password" class="am-radius"  placeholder="密码">
							    </div>
							    
		                        <div class="am-form-group ">
		                        	<button type="button" onclick="checkuser()" class="am-btn am-btn-primary am-radius" style="width: 100%;height: 100%;">登录</button>
		                        </div>
	                		</div>

	                	</form>
							
	                </div>
	            </div>
			</div>
		</div>


    <script type="text/javascript" src="/js/jquery.min.js"></script>
    <script type="text/javascript" src="/js/login.js"></script>
    
    <!-- 底部结束 -->

</body>
</html>