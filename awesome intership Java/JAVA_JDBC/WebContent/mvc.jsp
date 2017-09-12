<%@page import="java.io.IOException"%>
<%@page import="java.io.ObjectOutputStream"%>
<%@page import="java.io.FileOutputStream"%>
<%@page import="fiction.FictionBeanManager"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
         pageEncoding="ISO-8859-1"%>
<jsp:useBean id="hacker" class="fiction.Hacker"></jsp:useBean>
<jsp:useBean id="hero" class="fiction.Hero"></jsp:useBean>
<jsp:useBean id="mathematician" class="fiction.Mathematician"></jsp:useBean>
<jsp:useBean id="beanManager" class="fiction.FictionBeanManager"></jsp:useBean>
<jsp:useBean id="paminteanus" class="fiction.Pamintean"></jsp:useBean>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
</head>
<body>
<%
    String source = request.getParameter("namePage");//get name of current page
    if (source == null) {
%>
Sorry crapp happend
<%
} else {
    if (source.equals("addPage")) {
        //        out.println("Request from " + source);
        //do crazy stuff like
        String test = request.getParameter("fiction");
        try {
            if (test.equalsIgnoreCase("Hacker")) {
%>
<jsp:setProperty name="hacker" property="*" />
<p>Following data was setted</p>
Name:
<%=hacker.getName()%><br /> Fiction:
<%=hacker.getFiction()%>
<br /> What is special:
<%=hacker.getSpecial()%><br> Weapon:
<%=hacker.getWeapon()%><br>
<br /> Damge range:<%=hacker.doHarm()%><br /> toString:
<%=hacker.toString()%>

<%
    FictionBeanManager.add_s(hacker);
} else if (test.equals("Herp")) {
%>
<jsp:setProperty property="*" name="hero" />
<p>Following informations was setted</p>
toString:<%=hero.toString()%><br>

<%
    FictionBeanManager.add_s(hero);
} else if (test.equals("Mathematician")) {
%>
<jsp:setProperty property="*" name="mathematician" />
<p>Following information have been added</p>
toStirng:<%=mathematician.toString()%>

<%
    FictionBeanManager.add_s(mathematician);
} else if (test.equals("Pamintean")) {
%>
<jsp:setProperty property="*" name="paminteanus" />
<p>Following information have been added to database</p>
<%=paminteanus.toString()%>

<%
        beanManager.add(paminteanus);
    }
%>


<%
    } catch (Exception e) {
        out.println("Crappy stuff sometimes happened, I am sorry");
    }
} else if (source.equals("update.jsp"))
	//stream follow from update.jsp then 
{
    
        String whichAction = request.getParameter("submitButton");//whichi button was clicked
        String whichiIdShouldBeRemore = request
                .getParameter("prevId");

        if (whichAction.equals("deleted")){
            //call fictionBeanManager delete
            FictionBeanManager.remove(Integer.parseInt(whichiIdShouldBeRemore));
            out.println("deleted successful ");
%>
<jsp:forward page="doAll.jsp"></jsp:forward>
<%            
        }else{
            int id = Integer.parseInt(whichiIdShouldBeRemore);
            //doRemove
            FictionBeanManager.remove(id);
            String test = request.getParameter("fiction");
            try {
                if (test.equalsIgnoreCase("Hacker")) {
%>
<jsp:setProperty name="hacker" property="*" />
<p>Following data was setted</p>
Name:
<%=hacker.getName()%><br /> Fiction:
<%=hacker.getFiction()%>
<br /> What is special:
<%=hacker.getSpecial()%><br> Weapon:
<%=hacker.getWeapon()%><br>
<br /> Damge range:<%=hacker.doHarm()%><br /> toString:
<%=hacker.toString()%>

<%
    FictionBeanManager.add_s(hacker);
} else if (test.equals("Herp")) {
%>
<jsp:setProperty property="*" name="hero" />
<p>Following informations was setted</p>
toString:<%=hero.toString()%><br>

<%
    FictionBeanManager.add_s(hero);
} else if (test.equals("Mathematician")) {
%>
<jsp:setProperty property="*" name="mathematician" />
<p>Following information have been added</p>
toStirng:<%=mathematician.toString()%>

<%
    FictionBeanManager.add_s(mathematician);
} else if (test.equals("Pamintean")) {
%>
<jsp:setProperty property="*" name="paminteanus" />
<p>Following information have been added to database</p>
<%=paminteanus.toString()%>

<%
        beanManager.add(paminteanus);
    }
%>


<%
                    } catch (Exception e) {
                        out.println("Crappy stuff sometimes happened, I am sorry");
                    }
                    //detect type of fiction then added, if it is first just all add
                }

            }
        }
    

%>
<%!public void jspDestroy() {
    FictionBeanManager.SaveAll();
}%>


</body>
</html>