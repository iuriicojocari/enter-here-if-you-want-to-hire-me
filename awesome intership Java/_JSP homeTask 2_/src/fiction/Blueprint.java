package fiction;

import java.util.Random;

public abstract class Blueprint implements java.io.Serializable{

	String fiction;
	String name;
	 int weapon;
	String special;
	Random damge;
	
	public Blueprint(){
		damge = new Random();
	}
	
	public int getWepById(){
		return weapon;
	}
	
	public String getName() {
		return name;
	}
	
	public void setname(String name){
		this.name = name;
	}
	//public abstract void setname(String name);
		
	public abstract String getWeapon() ;
		
	public abstract void setweapon(int weapon) ;
		

	public String getSpecial() {
		return special;
	}

	public abstract void setSpecial(String special) ;

	public String getFiction() {
		return fiction;
	}
	
	public void setfiction(String Fiction){
		this.fiction = Fiction;
		
	}

	public abstract void setFiction(String fiction) ;

	public abstract int doHarm();
	
	
}
