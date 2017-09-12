<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Interesting assigments</title>
</head>

<body>
	<%!boolean b;
	boolean fromFIle;%>

	<%
		if (b == false) {
	%>

	<jsp:include page="myForm.jsp"></jsp:include>

	<%
		b = true;
	        } else {
	%>
	Your GPA is:
	<%
		ArrayList<Integer> myGrades = new ArrayList<>();
			//trying to parse an java file
	                try {
	                    myGrades.add(Integer.parseInt(request.getParameter("firstGrade")));
	                    myGrades.add(Integer.parseInt(request.getParameter("Computer sciences")));
	                    myGrades.add(Integer.parseInt(request.getParameter("topology")));
	                    myGrades.add(Integer.parseInt(request.getParameter("fAna")));
	                    myGrades.add(Integer.parseInt(request.getParameter("STL")));
	                    
	                    int i = 0;
	                    
	                    for (int iter:myGrades){
	                    	i+=iter;
	                    }
	                    //Trying to connect database for adding data there
	%>
	<%=i / 5%>
	<%
		} catch (NumberFormatException e) {
				b = false;
				out.println("It looks like you are tyring to hack ");
			}

		}
	%>

</body>
</html>