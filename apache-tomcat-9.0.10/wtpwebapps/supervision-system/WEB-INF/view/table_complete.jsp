<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>
<%@include file="/WEB-INF/common/taglibs.jsp"%>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>检索结果列表</title>
		<link rel="stylesheet" href="/css/amazeui.css" />
		<link rel="stylesheet" href="/css/font-awesome.min.css">
		<link rel="stylesheet" href="/css/core.css" />
		<link rel="stylesheet" href="/css/menu.css" />
		<link rel="stylesheet" href="/css/admin.css" />
		<link rel="stylesheet" href="/css/page/typography.css" />
		<link rel="stylesheet" href="/css/page/form.css" />
	</head>
	<body>
		<!-- Begin page -->
        <header class="am-topbar am-topbar-fixed-top">
          <div class="am-topbar-left am-hide-sm-only">
            <a href="/home" class="logo"><span style="color: #d8d8d8">舆情监督系统</span><i class="zmdi zmdi-layers"></i></a>
          </div>
         
          
          <!--最上面的横幅-->
          <div class="contain">
            <ul class="am-nav am-navbar-nav am-navbar-left">

              <li><h4 class="page-title">检索结果列表</h4></li>
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

		<!-- sidebar end -->
				
		<!-- ========== Left Sidebar end ========== -->
		
		
		
	<!--	<div class="am-g">-->
		<!-- ============================================================== -->
		<!-- Start right Content here -->
		<div class="content-page">
			<!-- Start content -->
			<div class="content">
				<div class="card-box">
					<!-- Row start -->
					<div class="am-g">
						<div class="am-u-sm-12 am-u-md-6">
				          <div class="am-btn-toolbar">
				            <div class="am-btn-group am-btn-group-xs">
				              <button type="button" class="am-btn am-btn-default"><span class="am-icon-plus"></span> 新增</button>
				              <button type="button" class="am-btn am-btn-default"><span class="am-icon-save"></span> 保存</button>
				              <button type="button" class="am-btn am-btn-default"><span class="am-icon-archive"></span> 审核</button>
				              <button type="button" class="am-btn am-btn-default"><span class="am-icon-trash-o"></span> 删除</button>
				            </div>
				          </div>
				        </div>	
				        
						<div class="am-u-sm-12 am-u-md-3">
				          <div class="am-input-group am-input-group-sm">
				            <input type="text" class="am-form-field">
				          <span class="am-input-group-btn">
				            <button class="am-btn am-btn-default" type="button">搜索</button>
				          </span>
				          </div>
				        </div>
				      </div>
					  <!-- Row end -->
					  
					  <!-- Row start -->
					  	<div class="am-g">
        <div class="am-u-sm-12">
          <form class="am-form">
            <table class="am-table am-table-striped am-table-hover table-main">
              <thead>
              <tr>
                <th class="table-id">序号</th>
                <th class="table-title">标题</th>
                <th class="table-type">数据来源</th>
                <th class="table-author am-hide-sm-only">内容</th>
                <th class="table-date am-hide-sm-only">发表时间</th>
                <th class="table-date am-hide-sm-only">点击率</th>
                <th class="table-date am-hide-sm-only">查看原网址</th>
              </tr>
              </thead>
              <tbody id="table_tbody">
              	<c:forEach items="${news}" var="newsItem">
					<tr>
						<td>${newsItem.id}</td>
						<td>${newsItem.title}</td>					
						<td>${newsItem.data_from}</td>
						<td>${newsItem.content}</td>
						<td>${newsItem.time}</td>
						<td>${newsItem.click}</td>
						<td><a href="${newsItem.url}">查看原网址...</a></td>
					</tr>
				</c:forEach>
              </tbody>
            </table>
            <div class="am-cf" >
              <div id='total_records'>共  条记录</div>
              <div class="am-fr" id="show_list">
                <ul class="am-pagination">
                  
                </ul>
              </div>
            </div>
          </form>
        </div>

      </div>
					  <!-- Row end -->					  
					</div>				
				</div>
			</div>
		</div>
		<!-- end right Content here -->
		<!--</div>-->
		</div>
		</div>
		
		<!-- navbar -->
		<a href="admin-offcanvas" class="am-icon-btn am-icon-th-list am-show-sm-only admin-menu" data-am-offcanvas="{target: '#admin-offcanvas'}"><!--<i class="fa fa-bars" aria-hidden="true"></i>--></a>
		
		<script type="text/javascript" src="/js/jquery-2.1.0.js" ></script>
		<script type="text/javascript" src="/js/table_complete.js"></script>
		<script type="text/javascript" src="/js/amazeui.min.js"></script>
		<script type="text/javascript" src="/js/app.js" ></script>
		<script type="text/javascript" src="/js/blockUI.js" ></script>
	</body>
	
</html>
