<%-- 
    Document   : tabel
    Created on : May 27, 2015, 9:19:20 PM
    Author     : YURIES
--%>

<%@page import="pojoclass.CatPOJO"%>
<%@page import="java.util.Iterator"%>
<%@page import="java.util.Collection"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<jsp:useBean id="pusher" class="imp.CatDAOImp" />
<jsp:useBean id="holder" class="pojoclass.CatPOJO"/>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <form method="GET" id="action_form" action="mvc.jsp"></form>
        <table style="width:100%" >
            <tr>
                <td>Cat id</td>
                <td>Name</td>
                <td>Color</td>
                <td>Age</td>
                <td>Action</td>
            </tr>
            <%
                Collection ar = pusher.getAllCats();
                if (ar != null) {
                    Iterator iterator = ar.iterator();
                    while (iterator.hasNext()) {
                        CatPOJO show = (CatPOJO) iterator.next();
                        holder = show;
//            following code should display nice table
            %>
            <tr>


                <td><input type="text" name="id" value="<%=holder.getId()%>" form="action_form"/></td>
                <td><input type="text" name="name" value="<%=holder.getName()%>" form="action_form"/></td>
                <td><input type="text" name="color" value="<%=holder.getColor()%>" form="action_form"/></td>
                <td><input type="text" name="age" value="<%=holder.getAge()%>" /></td>
                <td><input type="submit" name="buttonsaction" value="delete" form="action_form"/> | 
                    <input type="submit" name="buttonsaction" value="update" form="action_form"/>
                    <input type="hidden" name="source" value="update_or_del" form="action_form" />
                </td>
                <td>

                    <!--                    <form action="Update.jsp" method="post">
                                            <input type="submit" name="buttonsaction" value="delete"/> | 
                                            <input type="submit" name="buttonsaction" value="update"/>
                                            <input type="hidden" name="namePage" value="${pageContext.request.servletPath}">
                                            <input type="hidden" name="id" value="<%=holder.getId()%>">
                                        </form></td>-->


            </tr>

            <%
                    }
                } else {
                    out.println("We are working too hard to fix this issue, please forget about this page!");
                }
            %>
        </table>


    </body>
</html>
