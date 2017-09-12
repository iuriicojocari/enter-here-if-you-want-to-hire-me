//following script describes possible action for form
function chgAction(action_name)
{
    if (action_name == "mvc") {
        document.possible_action.action = "mvc.jsp";
        //next fragment set up sources
        document.getElementById("souces").value = "mainpage";

    }
    else if (action_name == "update") {
        document.possible_action.action = "update.jsp";
        document.getElementById("souces").value = "update";
    }
    else if (action_name == "ccc") {
        document.possible_action.action = "Hiber_CRUD_2/dele";
    }
}