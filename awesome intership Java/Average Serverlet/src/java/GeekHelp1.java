/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author YURIES
 */
@WebServlet(urlPatterns = {"/GeekHelp1"})
public class GeekHelp1 extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet GeekHelp works</title>");
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>Servlet GeekHelp\n\n at " + request.getContextPath() + "</h1>");
            out.println("</body>");
            out.println("</html>");

        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);

    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
        OutputStream oustream = response.getOutputStream();

        String height = request.getParameter("height");
        String weight = request.getParameter("weight");

        if (height == null || height.length() == 0) {
            throw new IllegalArgumentException("both height and weight require");
        }
        if (weight == null || weight.length() == 0) {
            throw new IllegalArgumentException("Weight is require ");
        }

        double hight_val = Double.valueOf(height);
        double weight_val = Double.valueOf(weight);

        if (hight_val == 0 || weight_val == 0) {
            throw new IllegalArgumentException("Height and Weight cannot be zero");
        }

        double bmi = (weight_val / (hight_val * hight_val)) * 703;

        String result = "<html><title>your bmi </title>"
                + "<body><h2>you're bmi index is " + Double.toString(bmi) + "</h2></body></html>";

//        oustream.print
        oustream.write(result.getBytes());

    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}



































