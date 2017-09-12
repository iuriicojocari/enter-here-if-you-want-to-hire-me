package fiction;

 

public class Hero extends Blueprint {

	@Override
	public String getWeapon() {
		// TODO Auto-generated method stub
		switch (super.weapon) {
		case 1:
			return "Laptop";
		case 2:
			return "Tablet";
		case 3:
			return "Mobile";
		}
		return "Unknown weapong with code " + super.weapon;
	}
	
	public void setweapon2012(int wp){
		setweapon(wp);
	}
	@Override
	public void setweapon(int weapon) {
		// TODO Auto-generated method stub
		super.weapon = weapon;
	}

	@Override
	public void setSpecial(String special) {
		// TODO Auto-generated method stub
		super.special = special;
	}

	@Override
	public void setFiction(String fiction) {
		// TODO Auto-generated method stub
		super.fiction = fiction;
	}

	@Override
	public int doHarm() {
		// TODO Auto-generated method stub
		return damge.nextInt(30) + 1;
	}

	@Override
	public void setname(String name) {
		// TODO Auto-generated method stubf
		super.name = name;

	}
	public void setShit(String name){
		super.name = name;
	}

	@Override
	public String toString() {
		return "Hero [fiction=" + fiction + ", name=" + name + ", weapon="
				+ weapon + ", special=" + special + "]";
	}

	@Override
	public int getcode() {
		// TODO Auto-generated method stub
		return 1;
	}

}
