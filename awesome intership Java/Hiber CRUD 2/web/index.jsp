<%-- 
    Document   : newjsp
    Created on : May 27, 2015, 11:03:08 AM
    Author     : YURIES
--%>


<%@page import="imp.CatDAOImp"%>
<%@page import="java.util.Collection"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <!--!!Atteiontion, this script is used to change action on form--> 
        <script type="text/javascript" src="script/possible_action.js">
        </script>
        
            <%--<jsp:include page="tabel.jsp"/>--%>
        
        <jsp:include page="form.jsp"/>
        <script>
            chgAction("mvc");
        </script>

    </body>
</html>
