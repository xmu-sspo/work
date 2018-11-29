<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>
<%@include file="/WEB-INF/common/taglibs.jsp"%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no">
    <title>关键词搜索</title>
    <link rel="stylesheet" href="/css/amazeui.css" />
    <link rel="stylesheet" href="/css/font-awesome.min.css">
    <link rel="stylesheet" href="/css/core.css" />
    <link rel="stylesheet" href="/css/menu.css" />
    <link rel="stylesheet" href="/css/admin.css" />
    <link rel="stylesheet" href="/css/page/typography.css" />

</head>
<body>
	<!-- Begin page -->
	<header class="am-topbar am-topbar-fixed-top">
	    <div class="am-topbar-left am-hide-sm-only">
	        <a href="/home" class="logo"><span style="color: #d8d8d8">舆情监督系统</span><i class="zmdi zmdi-layers"></i></a>
	    </div>
	
	    <div class="contain">
	        <ul class="am-nav am-navbar-nav am-navbar-left">
	
	            <li><h4 class="page-title">热度分析</h4></li>
	        </ul>
	
	        <ul class="am-nav am-navbar-nav am-navbar-right">
	            <li class="inform"><i class="am-icon-bell-o" aria-hidden="true"></i></li>
	            <li class="hidden-xs am-hide-sm-only">
	                <form role="search" class="app-search">
	                    <input type="text" placeholder="Search..." class="form-control">
	                    <a href=""><img src="/images/search.png"></a>
	                </form>
	            </li>
	        </ul>
	    </div>
	</header>
	<!-- end page -->
	
	
	<div class="admin">
	    <div class="admin-sidebar am-offcanvas  am-padding-10" id="admin-offcanvas">
	        <div class="am-offcanvas-bar admin-offcanvas-bar">
	            <!-- User -->
	            <div class="user-box am-hide-sm-only">
	                <div class="user-img">
	                    <img src="/images/avatar-1.jpg" id="user_img" alt="user-img" title="1111" class="img-circle img-thumbnail img-responsive">
	                    <div class="user-status offline"><i class="am-icon-dot-circle-o" aria-hidden="true"></i></div>
	                </div>
	                <h5><a href="#" id="user_name_a">zhy</a> </h5>
	                <ul class="list-inline">
	                    <li>
	                        <a href="#">
	                            <i class="fa fa-cog" aria-hidden="true"></i>
	                        </a>
	                    </li>
	
	                    <li>
	                        <a href="#" class="text-custom">
	                            <i class="fa fa-cog" aria-hidden="true"></i>
	                        </a>
	                    </li>
	                </ul>
	            </div>
	            <!-- End User -->
	
	            <!-- ========== 左侧菜单栏 ========== -->
	            <!-- sidebar start -->
	            <ul class="am-list admin-sidebar-list">
	                <li><a href="/home"><span class="am-icon-home"></span> 舆情检索</a></li>
	                <li class="admin-parent">
	                    <a class="am-cf" data-am-collapse="{target: '#collapse-nav1'}"><span class="am-icon-table"></span> 话题列表 <span class="am-icon-angle-right am-fr am-margin-right"></span></a>
	                    <ul class="am-list am-collapse admin-sidebar-sub am-in" id="collapse-nav1">
	                        <li><a href="/table_basic" class="am-cf"> 热门话题</a></li>
	                        <li><a href="/table_complete">新闻列表</a></li>
	                    </ul>
	                </li>
	                <li class="admin-parent">
	                    <a class="am-cf" data-am-collapse="{target: '#collapse-nav2'}"><i class="am-icon-line-chart" aria-hidden="true"></i>话题分析 <span class="am-icon-angle-right am-fr am-margin-right"></span></a>
	                    <ul class="am-list am-collapse admin-sidebar-sub am-in" id="collapse-nav2">
	                        <li><a href="/chart_line" class="am-cf"> 热度变化趋势图</a></li>
	                        <li><a href="/chart_pie" class="am-cf"> 发布平台分析图</a></li>
	                        <!--  <li><a href="/chart_columnar" class="am-cf"> 柱状图</a></li>
	                        <li><a href="/chart_pie" class="am-cf"> 饼状图</a></li>-->
	                    </ul>
	                </li>
	                <li class="admin-parent">
	                    <a class="am-cf" data-am-collapse="{target: '#collapse-nav5'}"><span class="am-icon-file"></span> 话题管理 <span class="am-icon-angle-right am-fr am-margin-right"></span></a>
	                    <ul class="am-list am-collapse admin-sidebar-sub am-in" id="collapse-nav5">
	                        <li><a href="/form_basic" class="am-cf"> 已关注话题</a></li>
	                        <li><a href="/form_validate">话题定制</a></li>
	                    </ul>
	                </li>
	
	            </ul>
	        </div>
	    </div>
	
	    <!-- ========== Left Sidebar end ========== -->
	    
	    <!-- Start right Content here -->
		<div class="content-page">
			<!-- Start content -->
			<div class="content">
			<div class="card-box">
				<div id="main" style="width: 100%;height:400px;"></div>
			</div>
			</div>
		</div>
		<!-- end right Content here -->
	</div>
	
	<script type="text/javascript" src="/js/jquery-2.1.0.js" ></script>
		<script type="text/javascript" src="/js/amazeui.min.js"></script>
		<script type="text/javascript" src="/js/app.js" ></script>
		<script type="text/javascript" src="/js/blockUI.js" ></script>
		<script type="text/javascript" src="/js/charts/echarts.js" ></script>
		<script type="text/javascript" src="/js/charts/line_diagram.js" ></script>
	</body>
	
</html>

</body>
</html>