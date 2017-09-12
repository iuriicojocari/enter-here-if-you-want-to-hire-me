package fiction;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

public class FictionBeanManager {
	static ArrayList<Blueprint> blueprints = new ArrayList<Blueprint>();
	static Connection conn = null;
	static Statement stmt = null;
	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
	static final String DB_URL = "jdbc:mysql://127.0.0.1/test";

	// Database credentials
	static final String USER = "root";
	static final String PASS = "secret";

	/**
	 * 
	 * @param Fiction_type
	 *            :String whichi reprezents the name of ficture
	 * @return Blueprint objects which is one of the following type [Hacker,
	 *         Hero, Pamintean, Mathematician] or in some case even null
	 */
	private Blueprint getOneObject(String Fiction_type) {
		Blueprint pusher = null;
		switch (Fiction_type) {
		case "Hacker":
			pusher = new Hacker();

		case "Herp":
			pusher = new Hero();

		case "Pamintean":
			pusher = new Pamintean();

		case "Mathematician":
			pusher = new Mathematician();

		}
		return pusher;

	}

	public FictionBeanManager() {
		try {
			// STEP 2: Register JDBC driver
			Class.forName("com.mysql.jdbc.Driver");

			// STEP 3: Open a connection
			System.out.println("Connecting to database...");
			conn = DriverManager.getConnection(DB_URL, USER, PASS);

			// STEP 4: Execute a query
			System.out.println("Creating statement...");
			stmt = conn.createStatement();
			String sql;
			sql = "SELECT * FROM fictions";
			ResultSet rs = stmt.executeQuery(sql);

			// STEP 5: Extract data from result set
			while (rs.next()) {
				// Retrieve by column name
				String Name = rs.getString("Name");
				String Fiction_type = rs.getString("Fiction type");
				int wepCode = rs.getInt("Weapon code");
				String special = rs.getString("Special");
				// System.out.println("name "+Name); debug purpose
				// here goes setter for this field
				Blueprint tempObj = getOneObject(Fiction_type);

				tempObj.setfiction(Fiction_type);
				tempObj.setname(Name);
				tempObj.setweapon(wepCode);
				tempObj.setSpecial(special);
				// System.out.println(tempObj); debug purpose
				blueprints.add(tempObj);
			}
			// STEP 6: Clean-up environment
			System.out.println("before cling up");
			// rs.close();
			// stmt.close();
			// conn.close();
			System.out.println("After");
		} catch (SQLException se) {
			// Handle errors for JDBC
			se.printStackTrace();
		} catch (Exception e) {
			// Handle errors for Class.forName
			e.printStackTrace();
		}
	}

	/**
	 * 
	 * @return connection
	 */

	public Connection getConnection() {
		try {
			conn = DriverManager.getConnection(DB_URL, USER, PASS);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				if (conn != null)
					conn.close();
			} catch (SQLException se) {
				se.printStackTrace();
			}// end finally try
		}
		return conn;
	}

	public static void add_s(Blueprint obj) {
		// ? add to database then push_back ?
		try {

			stmt = conn.createStatement();
			StringBuilder strB = new StringBuilder();

			System.out.println("Connecting to database from add_s");
			conn = DriverManager.getConnection(DB_URL, USER, PASS);

			strB.append("INSERT INTO fictions");
			strB.append(" value(");
			strB.append("\'" + obj.getName() + "\'");
			strB.append(",");
			strB.append("\'" + obj.getFiction() + "\'");
			strB.append(",");
			strB.append("\'" + obj.weapon + "\'");
			strB.append(",");
			strB.append("\'" + obj.special + "\'");
			strB.append(")");

			stmt.executeUpdate(strB.toString());
			blueprints.add(obj);

		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void add(Blueprint obj) {

		add_s(obj);

	}

	public static ArrayList<Blueprint> getBeansList() {
		return blueprints;
	}

	public static void insertAt(int start, Blueprint obj) {
		if (start < blueprints.size())
			blueprints.add(start, obj);
	}

	public static Blueprint getUserById(int id) {
		if (blueprints != null) {
			return blueprints.get(id);
		}
		return null;
	}

	public static void remove(Blueprint obj) {
		// reload list
		try {

			stmt = conn.createStatement();
			StringBuilder strB = new StringBuilder();

			System.out.println("Connecting to database from add_s");
			conn = DriverManager.getConnection(DB_URL, USER, PASS);
			System.out.println("Delete was been called with "+obj);
			strB.append("delete from fictions where Name = ");
			strB.append("\'" + obj.getName() + "\'");

			stmt.executeUpdate(strB.toString());
			blueprints.remove(obj);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static void remove(int index) {
		if (index < blueprints.size()) {

			remove(blueprints.get(index));
		}
	}

	public static void removeAll() {

	}

	public static void SaveAll() {
		// possible to force save
		try {
			FileOutputStream fos = new FileOutputStream("myfile.bin");
			ObjectOutputStream oos = new ObjectOutputStream(fos);
			oos.writeObject(FictionBeanManager.getBeansList());
			oos.close();
			fos.close();
		} catch (IOException ioe) {
			ioe.printStackTrace();
		}
	}

}
