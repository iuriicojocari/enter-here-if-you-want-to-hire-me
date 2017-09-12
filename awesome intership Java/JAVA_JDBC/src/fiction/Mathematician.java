package fiction;

 

public class Mathematician extends Blueprint {


	@Override
	public String getWeapon() {
		// TODO Auto-generated method stub
		switch (super.weapon) {
		case 9:
			return "chalk";
		case 10:
			return "Fields medal";
		case 11:
			return "books";
		case 12:
			return "Students";
		}
		return "shit";
	}
	
	public void setweapon2012(int w){
		super.weapon = w;
	}

	@Override
	public void setweapon(int weapon) {
		// TODO Auto-generated method stub
		super.weapon = weapon;
	}

	@Override
	public void setSpecial(String special) {
		// TODO Auto-generated method stub
		this.special = special;
	}

	@Override
	public void setFiction(String fiction) {
		// TODO Auto-generated method stub
		this.fiction = fiction;
	}

	@Override
	public int doHarm() {
		// TODO Auto-generated method stub
		return damge.nextInt(13)+3;
	}

	@Override
	public void setname(String name) {
		// TODO Auto-generated method stub
		super.name = name;
	}
	
	public void setShit(String name){
		super.name = name;
	}

	@Override
	public String toString() {
		return "Mathematician [fiction=" + fiction + ", name=" + name
				+ ", special=" + special + ", getWeapon()=" + getWeapon()
				+ ", doHarm()=" + doHarm() + "]";
	}

	@Override
	public int getcode() {
		// TODO Auto-generated method stub
		return 2;
	}
	
	
}
