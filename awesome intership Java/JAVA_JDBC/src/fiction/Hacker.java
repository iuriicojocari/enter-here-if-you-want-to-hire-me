package fiction;

 

public class Hacker extends Blueprint {

	public void setShit(String shit) {
		super.name = shit;
	}

	@Override
	public void setname(String name) {
		// TODO Auto-generated method stub
		super.name = name;
	}

	@Override
	public String getWeapon() {
		// TODO Auto-generated method stub
		switch (weapon) {
		case 1:
			return "Laptop";
		case 2:
			return "Tablet";
		case 3:
			return "Mobile";
		default:
			return "unknown weapong with id "+weapon;
		}

	}
	
	public void setweapon2012(int w){
		super.weapon =w;
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
		return damge.nextInt(13)+3;
	}

	@Override
	public String toString() {
		return "Hacker [fiction=" + fiction + ", name=" + name + ", special="
				+ special + ", getWeapon()=" + getWeapon() + ", doHarm()="
				+ doHarm() + "]";
	}

	@Override
	public int getcode() {
		// TODO Auto-generated method stub
		return 0;
	}

	
	
}
