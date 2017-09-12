package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import pojoclass.CatPOJO;
import java.util.Iterator;
import java.util.Collection;

public final class tabel_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      imp.CatDAOImp pusher = null;
      synchronized (_jspx_page_context) {
        pusher = (imp.CatDAOImp) _jspx_page_context.getAttribute("pusher", PageContext.PAGE_SCOPE);
        if (pusher == null){
          pusher = new imp.CatDAOImp();
          _jspx_page_context.setAttribute("pusher", pusher, PageContext.PAGE_SCOPE);
        }
      }
      out.write('\n');
      pojoclass.CatPOJO holder = null;
      synchronized (_jspx_page_context) {
        holder = (pojoclass.CatPOJO) _jspx_page_context.getAttribute("holder", PageContext.PAGE_SCOPE);
        if (holder == null){
          holder = new pojoclass.CatPOJO();
          _jspx_page_context.setAttribute("holder", holder, PageContext.PAGE_SCOPE);
        }
      }
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("        <title>JSP Page</title>\n");
      out.write("    </head>\n");
      out.write("    <body>\n");
      out.write("        <form method=\"GET\" id=\"action_form\" action=\"mvc.jsp\"></form>\n");
      out.write("        <table style=\"width:100%\" >\n");
      out.write("            <tr>\n");
      out.write("                <td>Cat id</td>\n");
      out.write("                <td>Name</td>\n");
      out.write("                <td>Color</td>\n");
      out.write("                <td>Age</td>\n");
      out.write("                <td>Action</td>\n");
      out.write("            </tr>\n");
      out.write("            ");

                Collection ar = pusher.getAllCats();
                if (ar != null) {
                    Iterator iterator = ar.iterator();
                    while (iterator.hasNext()) {
                        CatPOJO show = (CatPOJO) iterator.next();
                        holder = show;
//            following code should display nice table
            
      out.write("\n");
      out.write("            <tr>\n");
      out.write("\n");
      out.write("\n");
      out.write("                <td><input type=\"text\" name=\"id\" value=\"");
      out.print(holder.getId());
      out.write("\" form=\"action_form\"/></td>\n");
      out.write("                <td><input type=\"text\" name=\"name\" value=\"");
      out.print(holder.getName());
      out.write("\" form=\"action_form\"/></td>\n");
      out.write("                <td><input type=\"text\" name=\"color\" value=\"");
      out.print(holder.getColor());
      out.write("\" form=\"action_form\"/></td>\n");
      out.write("                <td><input type=\"text\" name=\"age\" value=\"");
      out.print(holder.getAge());
      out.write("\" /></td>\n");
      out.write("                <td><input type=\"submit\" name=\"buttonsaction\" value=\"delete\" form=\"action_form\"/> | \n");
      out.write("                    <input type=\"submit\" name=\"buttonsaction\" value=\"update\" form=\"action_form\"/>\n");
      out.write("                    <input type=\"hidden\" name=\"source\" value=\"update_or_del\" form=\"action_form\" />\n");
      out.write("                </td>\n");
      out.write("                <td>\n");
      out.write("\n");
      out.write("                    <!--                    <form action=\"Update.jsp\" method=\"post\">\n");
      out.write("                                            <input type=\"submit\" name=\"buttonsaction\" value=\"delete\"/> | \n");
      out.write("                                            <input type=\"submit\" name=\"buttonsaction\" value=\"update\"/>\n");
      out.write("                                            <input type=\"hidden\" name=\"namePage\" value=\"");
      out.write((java.lang.String) org.apache.jasper.runtime.PageContextImpl.evaluateExpression("${pageContext.request.servletPath}", java.lang.String.class, (PageContext)_jspx_page_context, null));
      out.write("\">\n");
      out.write("                                            <input type=\"hidden\" name=\"id\" value=\"");
      out.print(holder.getId());
      out.write("\">\n");
      out.write("                                        </form></td>-->\n");
      out.write("\n");
      out.write("\n");
      out.write("            </tr>\n");
      out.write("\n");
      out.write("            ");

                    }
                } else {
                    out.println("We are working too hard to fix this issue, please forget about this page!");
                }
            
      out.write("\n");
      out.write("        </table>\n");
      out.write("\n");
      out.write("\n");
      out.write("    </body>\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
