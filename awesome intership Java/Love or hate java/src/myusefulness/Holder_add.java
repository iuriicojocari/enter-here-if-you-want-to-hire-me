package myusefulness;

import java.security.SecureRandom;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

import org.apache.tomcat.dbcp.dbcp2.DriverManagerConnectionFactory;

public class Holder_add {
	Connection connect;
	Statement myStatment;

	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
	static final String DB_URL = "jdbc:mysql://www.db4free.net:3306/";

	// Database credentials
	static final String USER = "jdbctest2";
	static final String PASS = "jfhdsufpdsnjkdhsp";
	
	int topology;
	int computer_sciences;
	int math;
	int Functional_analisis;
	int stl;
	
	public void ConnectToDataBase() {
		
		
		try{
			
			connect = DriverManager.getConnection(DB_URL, USER, PASS);
			
		}catch(SQLException e){
//			out exception
		}
	}
	
	

}
