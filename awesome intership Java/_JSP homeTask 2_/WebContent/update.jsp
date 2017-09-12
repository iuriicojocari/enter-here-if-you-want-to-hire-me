<%@page import="fiction.FictionBeanManager"%>
<%@page import="fiction.Blueprint"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<%
		//this page should allow user to edit only user whichi was passed by request
		String edit = request.getParameter("edit");
		if (edit != null) {
			int id = Integer.parseInt(edit);
			Blueprint obj = FictionBeanManager.getUserById(id);
	%>
	<form action="mvc.jsp" method="post">
		Name: <input type="text" name="shit" value="<%=obj.getName()%>"><br />
		type:
		<!--  made default selected item -->
		<select name="fiction">
			<option value="<%=obj.getFiction()%>"><%=obj.getFiction()%></option>
		</select> <br /> Weapon: <select name="weapon2012">
			<option value="<%=obj.getWepById()%>"><%=obj.getWeapon()%></option>
		</select> <br /> What is special <input type="text" value="<%=obj.getSpecial() %>" name="special"> <br>
		<input type="hidden" name="namePage" value="update.jsp">
		<input type="hidden" name="prevId" value="<%=id%>">
		<input type="submit" name="submitButton" value="update" /><br>
		<input type="submit" name="submitButton" value="deleted" />		
	</form>
	<!-- call jspsetproperty -->
	<%
		} else {
	%>
	sorry try later
	<%
		}
	%>
</body>
</html>