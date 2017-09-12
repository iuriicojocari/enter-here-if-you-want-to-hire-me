package fiction;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

public class FictionBeanManager {
	static ArrayList<Blueprint> blueprints = new ArrayList<Blueprint>();

	public FictionBeanManager() {
		try {
			FileInputStream fis = new FileInputStream("myfile.bin");
			ObjectInputStream ois = new ObjectInputStream(fis);
			ArrayList<Blueprint> arraylist = new ArrayList<>();
			arraylist = (ArrayList) ois.readObject();
			blueprints = arraylist;
			ois.close();
			fis.close();
		} catch (IOException ioe) {
			// print something
		} catch (ClassNotFoundException c) {

			// do smthg
			return;
		}

	}

	public static void add_s(Blueprint obj) {
		blueprints.add(obj);
	}

	public void add(Blueprint obj) {
		blueprints.add(obj);
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
		if (blueprints != null) {
//			blueprints.remove(obj);
		}
	}

	public static void remove(int index) {
		if (index < blueprints.size()) {
			blueprints.remove(index);
		}
	}
	public static void removeAll(){
		
	}
	public static void SaveAll(){
		//possible to force save 
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
