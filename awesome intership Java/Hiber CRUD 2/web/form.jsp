<%-- 
    Document   : form
    Created on : May 27, 2015, 7:33:35 PM
    Author     : YURIES
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <form action="/"  accept-charset="UTF-8" method="get" name="possible_action" id="possible_action">
            Name:<input type="text" name="name"/><br />
            Color: <input type="text" name="color"/><br />
            Age: <input type="text" name="age" /><br />

            <input type="submit" value="done"/>
            <input type="hidden" name="source" id="souces" value=""/>
        </form>
    </body>
</html>
