<%-- 
    Document   : mvc
    Created on : May 27, 2015, 7:53:17 PM
    Author     : YURIES
--%>

<%@page import="pojoclass.CatPOJO"%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<jsp:useBean id="cat"  class="pojoclass.CatPOJO" ></jsp:useBean>
<jsp:useBean id="pusher" class="imp.CatDAOImp" ></jsp:useBean>

    <!DOCTYPE html>
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>Secreet pages</title>
        </head>
        <body>
        <%
            String source = request.getParameter("source");
            if (source == null) {
                out.println("is null");
            } else if (source.equalsIgnoreCase("mainpage")) {
        %>
        <jsp:setProperty property="*" name="cat"/>
        toString: <%=cat.toString()%>
        <%
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
        %>
        <jsp:setProperty property="*" name="cat"/>
        <%//call update
                            pusher.updateCat(id, cat);
                            out.println("success "+id);
                            break;
                    }
            }
        %>
    </body>
</html>
