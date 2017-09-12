<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
        <form action="Index.jsp" autocomplete="on" method="post">
            Math
            <input type="number" pattern="[^0-9]+[^*]" name="firstGrade" required="required" min="0" max="10"><br /> Computer
            Computer Science
            <input type="number" pattern="^[0-9]*$" name="Computer sciences" required="required" min="0" max="10"><br />
            Topology
            <input type="number" pattern="^[0-9]*$" name="topology" required="required" min="0" max="9"><br />
            Functional analysis
            <input type="number" pattern="^[0-9]*$" name="fAna" required="required" min="0" max="9"><br />
            STL
            <input type="number" pattern="^[0-9]*$" name="STL" required="required" min="0" max="9"><br />
            <!--add additional button which probably wont be used  -->
            <br> <input type="submit" value="Calculate GPA">
        </form>


</body>
</html>