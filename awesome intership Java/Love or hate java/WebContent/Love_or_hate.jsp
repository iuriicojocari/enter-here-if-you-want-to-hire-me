<%@page import="java.security.SecureRandom"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1" 
	mport="java.util.Random, java.security.SecureRandom" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<%
		//this is a declaration for prep swite variables
		SecureRandom r = new SecureRandom();
		int ch = r.nextInt(2);
	%>

	<%
		if (ch == 1) {
			out.println("I love programming in java language ");
	%>
	<%
		} else {
	%>
	Sometime I hate programming in java!!!
	<%
		}
	%>

	<!-- ${ch eq 1 ? "I love programming in java!!":"Sometimes I don't like programming in java especially when I don't know how to done that task in java" } -->


</body>
</html>