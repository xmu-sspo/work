/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/9.0.10
 * Generated at: 2018-07-26 07:03:31 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp.WEB_002dINF.view;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class form_005fvalidate_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {

  private static final javax.servlet.jsp.JspFactory _jspxFactory =
          javax.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  static {
    _jspx_dependants = new java.util.HashMap<java.lang.String,java.lang.Long>(5);
    _jspx_dependants.put("jar:file:/D:/work/apache-tomcat-9.0.10/webapps/supervision-system/WEB-INF/lib/jstl-impl-1.2.jar!/META-INF/fn.tld", Long.valueOf(1308098170000L));
    _jspx_dependants.put("jar:file:/D:/work/apache-tomcat-9.0.10/webapps/supervision-system/WEB-INF/lib/jstl-impl-1.2.jar!/META-INF/c.tld", Long.valueOf(1308098170000L));
    _jspx_dependants.put("/WEB-INF/common/taglibs.jsp", Long.valueOf(1531124938933L));
    _jspx_dependants.put("jar:file:/D:/work/apache-tomcat-9.0.10/webapps/supervision-system/WEB-INF/lib/jstl-impl-1.2.jar!/META-INF/fmt.tld", Long.valueOf(1308098170000L));
    _jspx_dependants.put("/WEB-INF/lib/jstl-impl-1.2.jar", Long.valueOf(1531052797107L));
  }

  private static final java.util.Set<java.lang.String> _jspx_imports_packages;

  private static final java.util.Set<java.lang.String> _jspx_imports_classes;

  static {
    _jspx_imports_packages = new java.util.HashSet<>();
    _jspx_imports_packages.add("javax.servlet");
    _jspx_imports_packages.add("javax.servlet.http");
    _jspx_imports_packages.add("javax.servlet.jsp");
    _jspx_imports_classes = null;
  }

  private org.apache.jasper.runtime.TagHandlerPool _005fjspx_005ftagPool_005fc_005fset_0026_005fvar_005fvalue_005fnobody;

  private volatile javax.el.ExpressionFactory _el_expressionfactory;
  private volatile org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.Map<java.lang.String,java.lang.Long> getDependants() {
    return _jspx_dependants;
  }

  public java.util.Set<java.lang.String> getPackageImports() {
    return _jspx_imports_packages;
  }

  public java.util.Set<java.lang.String> getClassImports() {
    return _jspx_imports_classes;
  }

  public javax.el.ExpressionFactory _jsp_getExpressionFactory() {
    if (_el_expressionfactory == null) {
      synchronized (this) {
        if (_el_expressionfactory == null) {
          _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
        }
      }
    }
    return _el_expressionfactory;
  }

  public org.apache.tomcat.InstanceManager _jsp_getInstanceManager() {
    if (_jsp_instancemanager == null) {
      synchronized (this) {
        if (_jsp_instancemanager == null) {
          _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
        }
      }
    }
    return _jsp_instancemanager;
  }

  public void _jspInit() {
    _005fjspx_005ftagPool_005fc_005fset_0026_005fvar_005fvalue_005fnobody = org.apache.jasper.runtime.TagHandlerPool.getTagHandlerPool(getServletConfig());
  }

  public void _jspDestroy() {
    _005fjspx_005ftagPool_005fc_005fset_0026_005fvar_005fvalue_005fnobody.release();
  }

  public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
      throws java.io.IOException, javax.servlet.ServletException {

    if (!javax.servlet.DispatcherType.ERROR.equals(request.getDispatcherType())) {
      final java.lang.String _jspx_method = request.getMethod();
      if ("OPTIONS".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        return;
      }
      if (!"GET".equals(_jspx_method) && !"POST".equals(_jspx_method) && !"HEAD".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED, "JSPs only permit GET, POST or HEAD. Jasper also permits OPTIONS");
        return;
      }
    }

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html; charset=utf-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write('\r');
      out.write('\n');
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write('\r');
      out.write('\n');
      if (_jspx_meth_c_005fset_005f0(_jspx_page_context))
        return;
      out.write('\r');
      out.write('\n');
      out.write('\r');
      out.write('\n');
      if (_jspx_meth_c_005fset_005f1(_jspx_page_context))
        return;
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write('\r');
      out.write('\n');
      if (_jspx_meth_c_005fset_005f2(_jspx_page_context))
        return;
      out.write(' ');
      out.write('\r');
      out.write('\n');
      out.write("\r\n");
      out.write("\r\n");
      out.write("<!DOCTYPE html>\r\n");
      out.write("<html>\r\n");
      out.write("\t<head>\r\n");
      out.write("\t\t<meta charset=\"utf-8\" />\r\n");
      out.write("\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\r\n");
      out.write("\t\t<title>后台模板</title>\r\n");
      out.write("\t\t<link rel=\"stylesheet\" href=\"/css/amazeui.css\" />\r\n");
      out.write("\t\t<link rel=\"stylesheet\" href=\"/css/font-awesome.min.css\">\r\n");
      out.write("\t\t<link rel=\"stylesheet\" href=\"/css/core.css\" />\r\n");
      out.write("\t\t<link rel=\"stylesheet\" href=\"/css/menu.css\" />\r\n");
      out.write("\t\t<link rel=\"stylesheet\" href=\"/css/index.css\" />\r\n");
      out.write("\t\t<link rel=\"stylesheet\" href=\"/css/admin.css\" />\r\n");
      out.write("\t\t<link rel=\"stylesheet\" href=\"/css/page/typography.css\" />\r\n");
      out.write("\t\t<link rel=\"stylesheet\" href=\"/css/page/form.css\" />\r\n");
      out.write("\t</head>\r\n");
      out.write("\t<body>\r\n");
      out.write("\t\t<!-- Begin page -->\r\n");
      out.write("\t\t<header class=\"am-topbar am-topbar-fixed-top\">\r\n");
      out.write("\t\t\t<div class=\"am-topbar-left am-hide-sm-only\">\r\n");
      out.write("\t\t\t\t<a href=\"/index\" class=\"logo\"><span style=\"color: #d8d8d8\">舆情监督系统</span><i class=\"zmdi zmdi-layers\"></i></a>\r\n");
      out.write("\t\t\t</div>\r\n");
      out.write("\t\r\n");
      out.write("\t\t\t<div class=\"contain\">\r\n");
      out.write("\t\t\t\t<ul class=\"am-nav am-navbar-nav am-navbar-left\">\r\n");
      out.write("\r\n");
      out.write("\t\t\t\t\t<li><h4 class=\"page-title\">表单验证</h4></li>\r\n");
      out.write("\t\t\t\t</ul>\r\n");
      out.write("\t\t\t\t\r\n");
      out.write("\t\t\t\t<ul class=\"am-nav am-navbar-nav am-navbar-right\">\r\n");
      out.write("\t\t\t\t\t<li class=\"inform\"><i class=\"am-icon-bell-o\" aria-hidden=\"true\"></i></li>\r\n");
      out.write("\t\t\t\t\t<li class=\"hidden-xs am-hide-sm-only\">\r\n");
      out.write("                        <form role=\"search\" class=\"app-search\">\r\n");
      out.write("                            <input type=\"text\" placeholder=\"Search...\" class=\"form-control\">\r\n");
      out.write("                            <a href=\"\"><img src=\"/images/search.png\"></a>\r\n");
      out.write("                        </form>\r\n");
      out.write("                    </li>\r\n");
      out.write("\t\t\t\t</ul>\r\n");
      out.write("\t\t\t</div>\r\n");
      out.write("\t\t</header>\r\n");
      out.write("\t\t<!-- end page -->\r\n");
      out.write("\t\t\r\n");
      out.write("\t\t\r\n");
      out.write("\t\t<div class=\"admin\">\r\n");
      out.write("\t\t\t<!--<div class=\"am-g\">-->\r\n");
      out.write("\t\t<!-- ========== Left Sidebar Start ========== -->\r\n");
      out.write("\t\t<!--<div class=\"left side-menu am-hide-sm-only am-u-md-1 am-padding-0\">\r\n");
      out.write("\t\t\t<div class=\"slimScrollDiv\" style=\"position: relative; overflow: hidden; width: auto; height: 548px;\">\r\n");
      out.write("\t\t\t\t<div class=\"sidebar-inner slimscrollleft\" style=\"overflow: hidden; width: auto; height: 548px;\">-->\r\n");
      out.write("                  <!-- sidebar start -->\r\n");
      out.write("\t\t\t\t  <div class=\"admin-sidebar am-offcanvas  am-padding-0\" id=\"admin-offcanvas\">\r\n");
      out.write("\t\t\t\t    <div class=\"am-offcanvas-bar admin-offcanvas-bar\">\r\n");
      out.write("\t            \r\n");
      out.write("\t\t\t\t\t\t <ul class=\"am-list admin-sidebar-list\">\r\n");
      out.write("\t\t\t\t\t\t    <li><a href=\"/index\"><span class=\"am-icon-home\"></span> 首页</a></li>\r\n");
      out.write("\t\t\t\t\t\t    <li class=\"admin-parent\">\r\n");
      out.write("\t\t\t\t\t\t      <a class=\"am-cf\" data-am-collapse=\"{target: '#collapse-nav1'}\"><span class=\"am-icon-table\"></span> 话题列表 <span class=\"am-icon-angle-right am-fr am-margin-right\"></span></a>\r\n");
      out.write("\t\t\t\t\t\t      <ul class=\"am-list am-collapse admin-sidebar-sub am-in\" id=\"collapse-nav1\">\r\n");
      out.write("\t\t\t\t\t\t        <li><a href=\"/table_basic\" class=\"am-cf\"> 基本表格</span></a></li>\r\n");
      out.write("\t\t\t\t\t\t        <li><a href=\"/table_complete\">完整表格</a></li>\r\n");
      out.write("\t\t\t\t\t\t      </ul>\r\n");
      out.write("\t\t\t\t\t\t    </li>\r\n");
      out.write("\t\t\t\t\t\t    <li class=\"admin-parent\">\r\n");
      out.write("\t\t\t\t\t\t      <a class=\"am-cf\" data-am-collapse=\"{target: '#collapse-nav2'}\"><i class=\"am-icon-line-chart\" aria-hidden=\"true\"></i> 统计图表 <span class=\"am-icon-angle-right am-fr am-margin-right\"></span></a>\r\n");
      out.write("\t\t\t\t\t\t      <ul class=\"am-list am-collapse admin-sidebar-sub am-in\" id=\"collapse-nav2\">\r\n");
      out.write("\t\t\t\t\t\t        <li><a href=\"/chart_line\" class=\"am-cf\"> 折线图</span></a></li>\r\n");
      out.write("\t\t\t\t\t\t        <li><a href=\"/chart_columnar\" class=\"am-cf\"> 柱状图</span></a></li>\r\n");
      out.write("\t\t\t\t\t\t        <li><a href=\"/chart_pie\" class=\"am-cf\"> 饼状图</span></a></li>\r\n");
      out.write("\t\t\t\t\t\t      </ul>\r\n");
      out.write("\t\t\t\t\t\t    </li>\r\n");
      out.write("\t\t\t\t\t\t    <li class=\"admin-parent\">\r\n");
      out.write("\t\t\t\t\t\t      <a class=\"am-cf\" data-am-collapse=\"{target: '#collapse-nav5'}\"><span class=\"am-icon-file\"></span> 表单 <span class=\"am-icon-angle-right am-fr am-margin-right\"></span></a>\r\n");
      out.write("\t\t\t\t\t\t      <ul class=\"am-list am-collapse admin-sidebar-sub am-in\" id=\"collapse-nav5\">\r\n");
      out.write("\t\t\t\t\t\t        <li><a href=\"/form_basic\" class=\"am-cf\"> 基本表单</a></li>\r\n");
      out.write("\t\t\t\t\t\t        <li><a href=\"/form_validate\">表单验证</a></li>   \r\n");
      out.write("\t\t\t\t\t\t      </ul>\r\n");
      out.write("\t\t\t\t\t\t    </li>\r\n");
      out.write("\t\t\t\t\t\t  </ul>\r\n");
      out.write("\t\t\t\t</div>\r\n");
      out.write("\t\t\t\t  </div>\r\n");
      out.write("\t\t\t\t  <!-- sidebar end -->\r\n");
      out.write("    \r\n");
      out.write("\t\t\t\t<!--</div>\r\n");
      out.write("\t\t\t</div>\r\n");
      out.write("\t\t</div>-->\r\n");
      out.write("\t\t<!-- ========== Left Sidebar end ========== -->\r\n");
      out.write("\t\t\r\n");
      out.write("\t\t\r\n");
      out.write("\t\t\r\n");
      out.write("\t<!--\t<div class=\"am-g\">-->\r\n");
      out.write("\t\t<!-- ============================================================== -->\r\n");
      out.write("\t\t<!-- Start right Content here -->\r\n");
      out.write("\t\t<div class=\"content-page\">\r\n");
      out.write("\t\t\t<!-- Start content -->\r\n");
      out.write("\t\t\t<div class=\"content\">\r\n");
      out.write("\t\t\t\t<div class=\"am-g\">\r\n");
      out.write("\t\t\t\t\t<!-- Row start -->\r\n");
      out.write("\t\t\t\t\t\t<div class=\"am-u-sm-12\">\r\n");
      out.write("\t\t\t\t\t\t\t<div class=\"card-box\">\r\n");
      out.write("\t\t\t\t\t\t\t\t<ul class=\"am-nav am-fr\">\r\n");
      out.write("\t\t\t\t\t\t\t\t  <li class=\"am-dropdown\" data-am-dropdown>\r\n");
      out.write("\t\t\t\t\t\t\t\t    <a class=\"am-dropdown-toggle\" data-am-dropdown-toggle href=\"javascript:;\">\r\n");
      out.write("\t\t\t\t\t\t\t\t       <span class=\"am-icon-caret-down\"></span>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </a>\r\n");
      out.write("\t\t\t\t\t\t\t\t    <ul class=\"am-dropdown-content\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <li>1231234</li>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <li>1231234</li>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <li>1231234</li>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <li>1231234</li>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </ul>\r\n");
      out.write("\t\t\t\t\t\t\t\t  </li>\r\n");
      out.write("\t\t\t\t\t\t\t\t</ul>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t<form action=\"\" class=\"am-form\" data-am-validator>\r\n");
      out.write("\t\t\t\t\t\t\t\t  <fieldset>\r\n");
      out.write("\t\t\t\t\t\t\t\t    <legend>JS 表单验证</legend>\r\n");
      out.write("\t\t\t\t\t\t\t\t    <div class=\"am-form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label for=\"doc-vld-name-2\">用户名：</label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <input type=\"text\" id=\"doc-vld-name-2\" minlength=\"3\" placeholder=\"输入用户名（至少 3 个字符）\" required/>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </div>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t    <div class=\"am-form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label for=\"doc-vld-email-2\">邮箱：</label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <input type=\"email\" id=\"doc-vld-email-2\" placeholder=\"输入邮箱\" required/>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </div>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t    <div class=\"am-form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label for=\"doc-vld-url-2\">网址：</label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <input type=\"url\" id=\"doc-vld-url-2\" placeholder=\"输入网址\" required/>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </div>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t    <div class=\"am-form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label for=\"doc-vld-age-2\">年龄：</label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <input type=\"number\" class=\"\"  id=\"doc-vld-age-2\" placeholder=\"输入年龄  18-120\" min=\"18\" max=\"120\" required />\r\n");
      out.write("\t\t\t\t\t\t\t\t    </div>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t    <div class=\"am-form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label class=\"am-form-label\">爱好：</label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label class=\"am-checkbox-inline\">\r\n");
      out.write("\t\t\t\t\t\t\t\t        <input type=\"checkbox\" value=\"橘子\" name=\"docVlCb\" minchecked=\"2\" maxchecked=\"4\" required> 橘子\r\n");
      out.write("\t\t\t\t\t\t\t\t      </label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label class=\"am-checkbox-inline\">\r\n");
      out.write("\t\t\t\t\t\t\t\t        <input type=\"checkbox\" value=\"苹果\" name=\"docVlCb\"> 苹果\r\n");
      out.write("\t\t\t\t\t\t\t\t      </label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label class=\"am-checkbox-inline\">\r\n");
      out.write("\t\t\t\t\t\t\t\t        <input type=\"checkbox\" value=\"菠萝\" name=\"docVlCb\"> 菠萝\r\n");
      out.write("\t\t\t\t\t\t\t\t      </label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label class=\"am-checkbox-inline\">\r\n");
      out.write("\t\t\t\t\t\t\t\t        <input type=\"checkbox\" value=\"芒果\" name=\"docVlCb\"> 芒果\r\n");
      out.write("\t\t\t\t\t\t\t\t      </label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label class=\"am-checkbox-inline\">\r\n");
      out.write("\t\t\t\t\t\t\t\t        <input type=\"checkbox\" value=\"香蕉\" name=\"docVlCb\"> 香蕉\r\n");
      out.write("\t\t\t\t\t\t\t\t      </label>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </div>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t    <div class=\"am-form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label>性别： </label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label class=\"am-radio-inline\">\r\n");
      out.write("\t\t\t\t\t\t\t\t        <input type=\"radio\"  value=\"\" name=\"docVlGender\" required> 男\r\n");
      out.write("\t\t\t\t\t\t\t\t      </label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label class=\"am-radio-inline\">\r\n");
      out.write("\t\t\t\t\t\t\t\t        <input type=\"radio\" name=\"docVlGender\"> 女\r\n");
      out.write("\t\t\t\t\t\t\t\t      </label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label class=\"am-radio-inline\">\r\n");
      out.write("\t\t\t\t\t\t\t\t        <input type=\"radio\" name=\"docVlGender\"> 其他\r\n");
      out.write("\t\t\t\t\t\t\t\t      </label>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </div>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t    <div class=\"am-form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label for=\"doc-select-1\">下拉单选框</label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <select id=\"doc-select-1\" required>\r\n");
      out.write("\t\t\t\t\t\t\t\t        <option value=\"\">-=请选择一项=-</option>\r\n");
      out.write("\t\t\t\t\t\t\t\t        <option value=\"option1\">选项一...</option>\r\n");
      out.write("\t\t\t\t\t\t\t\t        <option value=\"option2\">选项二.....</option>\r\n");
      out.write("\t\t\t\t\t\t\t\t        <option value=\"option3\">选项三........</option>\r\n");
      out.write("\t\t\t\t\t\t\t\t      </select>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <span class=\"am-form-caret\"></span>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </div>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t    <div class=\"am-form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label for=\"doc-select-2\">多选框</label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <select multiple class=\"\" id=\"doc-select-2\" minchecked=\"2\" maxchecked=\"4\">\r\n");
      out.write("\t\t\t\t\t\t\t\t        <option>1</option>\r\n");
      out.write("\t\t\t\t\t\t\t\t        <option>2</option>\r\n");
      out.write("\t\t\t\t\t\t\t\t        <option>3</option>\r\n");
      out.write("\t\t\t\t\t\t\t\t        <option>4</option>\r\n");
      out.write("\t\t\t\t\t\t\t\t        <option>5</option>\r\n");
      out.write("\t\t\t\t\t\t\t\t      </select>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </div>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t    <div class=\"am-form-group\">\r\n");
      out.write("\t\t\t\t\t\t\t\t      <label for=\"doc-vld-ta-2\">评论：</label>\r\n");
      out.write("\t\t\t\t\t\t\t\t      <textarea id=\"doc-vld-ta-2\" minlength=\"10\" maxlength=\"100\"></textarea>\r\n");
      out.write("\t\t\t\t\t\t\t\t    </div>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t    <button class=\"am-btn am-btn-secondary\" type=\"submit\">提交</button>\r\n");
      out.write("\t\t\t\t\t\t\t\t  </fieldset>\r\n");
      out.write("\t\t\t\t\t\t\t\t</form>\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t\t\r\n");
      out.write("\t\t\t\t\t\t\t</div>\r\n");
      out.write("\t\t\t\t\t\t</div>\r\n");
      out.write("\t\t\t\t\t<!-- Row end -->\r\n");
      out.write("\t\t\t\t</div>\r\n");
      out.write("\t\t\t\r\n");
      out.write("\t\t\t\r\n");
      out.write("\t\t\t\r\n");
      out.write("\t\t\t\r\n");
      out.write("\t\t\t</div>\r\n");
      out.write("\t\t</div>\r\n");
      out.write("\t\t<!-- end right Content here -->\r\n");
      out.write("\t\t<!--</div>-->\r\n");
      out.write("\t\t</div>\r\n");
      out.write("\t\t</div>\r\n");
      out.write("\t\t\r\n");
      out.write("\t\t<!-- navbar -->\r\n");
      out.write("\t\t<a href=\"admin-offcanvas\" class=\"am-icon-btn am-icon-th-list am-show-sm-only admin-menu\" data-am-offcanvas=\"{target: '#admin-offcanvas'}\"><!--<i class=\"fa fa-bars\" aria-hidden=\"true\"></i>--></a>\r\n");
      out.write("\t\t\r\n");
      out.write("\t\t<script type=\"text/javascript\" src=\"/js/jquery-2.1.0.js\" ></script>\r\n");
      out.write("\t\t<script type=\"text/javascript\" src=\"/js/amazeui.min.js\"></script>\r\n");
      out.write("\t\t<script type=\"text/javascript\" src=\"/js/app.js\" ></script>\r\n");
      out.write("\t\t<script type=\"text/javascript\" src=\"/js/blockUI.js\" ></script>\r\n");
      out.write("\t</body>\r\n");
      out.write("\t\r\n");
      out.write("</html>\r\n");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try {
            if (response.isCommitted()) {
              out.flush();
            } else {
              out.clearBuffer();
            }
          } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }

  private boolean _jspx_meth_c_005fset_005f0(javax.servlet.jsp.PageContext _jspx_page_context)
          throws java.lang.Throwable {
    javax.servlet.jsp.PageContext pageContext = _jspx_page_context;
    javax.servlet.jsp.JspWriter out = _jspx_page_context.getOut();
    //  c:set
    org.apache.taglibs.standard.tag.rt.core.SetTag _jspx_th_c_005fset_005f0 = (org.apache.taglibs.standard.tag.rt.core.SetTag) _005fjspx_005ftagPool_005fc_005fset_0026_005fvar_005fvalue_005fnobody.get(org.apache.taglibs.standard.tag.rt.core.SetTag.class);
    boolean _jspx_th_c_005fset_005f0_reused = false;
    try {
      _jspx_th_c_005fset_005f0.setPageContext(_jspx_page_context);
      _jspx_th_c_005fset_005f0.setParent(null);
      // /WEB-INF/common/taglibs.jsp(5,0) name = var type = java.lang.String reqTime = false required = false fragment = false deferredValue = false expectedTypeName = null deferredMethod = false methodSignature = null
      _jspx_th_c_005fset_005f0.setVar("ctx");
      // /WEB-INF/common/taglibs.jsp(5,0) name = value type = javax.el.ValueExpression reqTime = true required = false fragment = false deferredValue = true expectedTypeName = java.lang.Object deferredMethod = false methodSignature = null
      _jspx_th_c_005fset_005f0.setValue(new org.apache.jasper.el.JspValueExpression("/WEB-INF/common/taglibs.jsp(5,0) '${pageContext.request.contextPath}'",_jsp_getExpressionFactory().createValueExpression(_jspx_page_context.getELContext(),"${pageContext.request.contextPath}",java.lang.Object.class)).getValue(_jspx_page_context.getELContext()));
      int _jspx_eval_c_005fset_005f0 = _jspx_th_c_005fset_005f0.doStartTag();
      if (_jspx_th_c_005fset_005f0.doEndTag() == javax.servlet.jsp.tagext.Tag.SKIP_PAGE) {
        return true;
      }
      _005fjspx_005ftagPool_005fc_005fset_0026_005fvar_005fvalue_005fnobody.reuse(_jspx_th_c_005fset_005f0);
      _jspx_th_c_005fset_005f0_reused = true;
    } finally {
      org.apache.jasper.runtime.JspRuntimeLibrary.releaseTag(_jspx_th_c_005fset_005f0, _jsp_getInstanceManager(), _jspx_th_c_005fset_005f0_reused);
    }
    return false;
  }

  private boolean _jspx_meth_c_005fset_005f1(javax.servlet.jsp.PageContext _jspx_page_context)
          throws java.lang.Throwable {
    javax.servlet.jsp.PageContext pageContext = _jspx_page_context;
    javax.servlet.jsp.JspWriter out = _jspx_page_context.getOut();
    //  c:set
    org.apache.taglibs.standard.tag.rt.core.SetTag _jspx_th_c_005fset_005f1 = (org.apache.taglibs.standard.tag.rt.core.SetTag) _005fjspx_005ftagPool_005fc_005fset_0026_005fvar_005fvalue_005fnobody.get(org.apache.taglibs.standard.tag.rt.core.SetTag.class);
    boolean _jspx_th_c_005fset_005f1_reused = false;
    try {
      _jspx_th_c_005fset_005f1.setPageContext(_jspx_page_context);
      _jspx_th_c_005fset_005f1.setParent(null);
      // /WEB-INF/common/taglibs.jsp(7,0) name = var type = java.lang.String reqTime = false required = false fragment = false deferredValue = false expectedTypeName = null deferredMethod = false methodSignature = null
      _jspx_th_c_005fset_005f1.setVar("jcPath");
      // /WEB-INF/common/taglibs.jsp(7,0) name = value type = javax.el.ValueExpression reqTime = true required = false fragment = false deferredValue = true expectedTypeName = java.lang.Object deferredMethod = false methodSignature = null
      _jspx_th_c_005fset_005f1.setValue(new org.apache.jasper.el.JspValueExpression("/WEB-INF/common/taglibs.jsp(7,0) '${pageContext.request.contextPath}'",_jsp_getExpressionFactory().createValueExpression(_jspx_page_context.getELContext(),"${pageContext.request.contextPath}",java.lang.Object.class)).getValue(_jspx_page_context.getELContext()));
      int _jspx_eval_c_005fset_005f1 = _jspx_th_c_005fset_005f1.doStartTag();
      if (_jspx_th_c_005fset_005f1.doEndTag() == javax.servlet.jsp.tagext.Tag.SKIP_PAGE) {
        return true;
      }
      _005fjspx_005ftagPool_005fc_005fset_0026_005fvar_005fvalue_005fnobody.reuse(_jspx_th_c_005fset_005f1);
      _jspx_th_c_005fset_005f1_reused = true;
    } finally {
      org.apache.jasper.runtime.JspRuntimeLibrary.releaseTag(_jspx_th_c_005fset_005f1, _jsp_getInstanceManager(), _jspx_th_c_005fset_005f1_reused);
    }
    return false;
  }

  private boolean _jspx_meth_c_005fset_005f2(javax.servlet.jsp.PageContext _jspx_page_context)
          throws java.lang.Throwable {
    javax.servlet.jsp.PageContext pageContext = _jspx_page_context;
    javax.servlet.jsp.JspWriter out = _jspx_page_context.getOut();
    //  c:set
    org.apache.taglibs.standard.tag.rt.core.SetTag _jspx_th_c_005fset_005f2 = (org.apache.taglibs.standard.tag.rt.core.SetTag) _005fjspx_005ftagPool_005fc_005fset_0026_005fvar_005fvalue_005fnobody.get(org.apache.taglibs.standard.tag.rt.core.SetTag.class);
    boolean _jspx_th_c_005fset_005f2_reused = false;
    try {
      _jspx_th_c_005fset_005f2.setPageContext(_jspx_page_context);
      _jspx_th_c_005fset_005f2.setParent(null);
      // /WEB-INF/common/taglibs.jsp(19,0) name = var type = java.lang.String reqTime = false required = false fragment = false deferredValue = false expectedTypeName = null deferredMethod = false methodSignature = null
      _jspx_th_c_005fset_005f2.setVar("mainPath");
      // /WEB-INF/common/taglibs.jsp(19,0) name = value type = javax.el.ValueExpression reqTime = true required = false fragment = false deferredValue = true expectedTypeName = java.lang.Object deferredMethod = false methodSignature = null
      _jspx_th_c_005fset_005f2.setValue(new org.apache.jasper.el.JspValueExpression("/WEB-INF/common/taglibs.jsp(19,0) '${mainBasePath}'",_jsp_getExpressionFactory().createValueExpression(_jspx_page_context.getELContext(),"${mainBasePath}",java.lang.Object.class)).getValue(_jspx_page_context.getELContext()));
      int _jspx_eval_c_005fset_005f2 = _jspx_th_c_005fset_005f2.doStartTag();
      if (_jspx_th_c_005fset_005f2.doEndTag() == javax.servlet.jsp.tagext.Tag.SKIP_PAGE) {
        return true;
      }
      _005fjspx_005ftagPool_005fc_005fset_0026_005fvar_005fvalue_005fnobody.reuse(_jspx_th_c_005fset_005f2);
      _jspx_th_c_005fset_005f2_reused = true;
    } finally {
      org.apache.jasper.runtime.JspRuntimeLibrary.releaseTag(_jspx_th_c_005fset_005f2, _jsp_getInstanceManager(), _jspx_th_c_005fset_005f2_reused);
    }
    return false;
  }
}
