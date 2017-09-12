<%@page import="fiction.FictionBeanManager"%>
<%@page import="fiction.Blueprint"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>CRUD(Create Read Update Delete)</title>
<script
	src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
</head>
<body>
	<br>
	<!-- list of all items in -->
	<%
		ArrayList<Blueprint> pritns;
		pritns = FictionBeanManager.getBeansList();
		if (!pritns.isEmpty()) {
			//prints all name with lick to edit
			int i = 0;
			StringBuilder strb = new StringBuilder();
			for (Blueprint bl : pritns) {
				strb.append("<a href=");//a href=
				strb.append("\"");// a href="
				strb.append("update.jsp");//a href="edit.jsp
				strb.append("?edit=");//a href=edit.jsp?edit=
				strb.append(i);// a href="edit.jsp?edit=i
				strb.append("\"");//a href="edit.jsp?edit=i"
				strb.append(">");
				strb.append(bl.getName());
				strb.append("</a>");
				out.println(strb.toString());
				i++;
				strb.setLength(0);

			}
		}
	%><br />
	<form action="mvc.jsp" method="get">
		Name: <input type="text" name="shit"><br /> type:<select
			name="fiction">
			<option value="nonselected"></option>
			<option value="Hacker">Hacker</option>
			<option value="Herp">Hero</option>
			<option value="Pamintean">Pamintean</option>
			<option value="Mathematician">Mathematician</option>
		</select> <br /> Weapon: <select name="weapon2012">
			<optgroup label="Hacker weapon">
				<option value="1">Laptop</option>
				<option value="2">Table</option>
				<option value="3">Mobile</option>
			</optgroup>
			<optgroup label="Hero weapon">
				<option value="4">Sword</option>
				<option value="5">Lock</option>
			</optgroup>
			<optgroup label="Pamintean">
				<option value="7">Computer</option>
				<option value="8">other</option>
			</optgroup>
			<optgroup label="Mathematician">
				<option value="9">chalk</option>
				<option value="10">Field medal</option>
				<option value="11">books</option>
			</optgroup>
		</select> <br /> What is special <input type="text" name="special"> <br>
		<input type="hidden" name="namePage" value="addPage">
		<input type="submit" id="hiddenSubmit">
	</form>


	<!-- 	<script type="text/javascript">
		$("#hiddenSubmit").hide();
		$("#fiction").change(function() {
			var val = $("#fiction").val();

			if (val != "nonselected") {

				$("#hiddenSubmit").show();
			}
		});
	</script>
 -->


</body>
</html>