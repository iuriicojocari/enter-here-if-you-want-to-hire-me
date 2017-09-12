package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import pojoclass.CatPOJO;

public final class mvc_jsp extends org.apache.jasper.runtime.HttpJspBase
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
      pojoclass.CatPOJO cat = null;
      synchronized (_jspx_page_context) {
        cat = (pojoclass.CatPOJO) _jspx_page_context.getAttribute("cat", PageContext.PAGE_SCOPE);
        if (cat == null){
          cat = new pojoclass.CatPOJO();
          _jspx_page_context.setAttribute("cat", cat, PageContext.PAGE_SCOPE);
        }
      }
      out.write('\n');
      imp.CatDAOImp pusher = null;
      synchronized (_jspx_page_context) {
        pusher = (imp.CatDAOImp) _jspx_page_context.getAttribute("pusher", PageContext.PAGE_SCOPE);
        if (pusher == null){
          pusher = new imp.CatDAOImp();
          _jspx_page_context.setAttribute("pusher", pusher, PageContext.PAGE_SCOPE);
        }
      }
      out.write("\n");
      out.write("\n");
      out.write("    <!DOCTYPE html>\n");
      out.write("    <html>\n");
      out.write("        <head>\n");
      out.write("            <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("            <title>Secreet pages</title>\n");
      out.write("        </head>\n");
      out.write("        <body>\n");
      out.write("        ");

            String source = request.getParameter("source");
            if (source == null) {
                out.println("is null");
            } else if (source.equalsIgnoreCase("mainpage")) {
        
      out.write("\n");
      out.write("        ");
      org.apache.jasper.runtime.JspRuntimeLibrary.introspect(_jspx_page_context.findAttribute("cat"), request);
      out.write("\n");
      out.write("        toString: ");
      out.print(cat.toString());
      out.write("\n");
      out.write("        ");

            pusher.addCat(cat);
        } else if (source.equalsIgnoreCase("update")) {
            out.print("update");
        } else if (source.equalsIgnoreCase("update_or_del")) {
            String whichButton = request.getParameter("buttonsaction");
            Long id = Long.parseLong(request.getParameter("id"));
            if (whichButton != null)
                switch (whichButton) {
                    case "delete"://call delete 
                        pusher.DeleteCatById(id);
                        out.println("success " + id);
                        break;
                    case "update":
        
      out.write("\n");
      out.write("        ");
      org.apache.jasper.runtime.JspRuntimeLibrary.introspect(_jspx_page_context.findAttribute("cat"), request);
      out.write("\n");
      out.write("        ");
//call update
                            pusher.updateCat(id, cat);
                            
                            break;
                    }
            }
        
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
