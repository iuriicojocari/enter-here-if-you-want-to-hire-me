package fiction;

public class Pamintean extends Blueprint {

	@Override
	public String getWeapon() {
		// TODO Auto-generated method stub
		switch (weapon) {
		case 7:
			return "computer";
		case 8:
			return "other";
		}
		return "Unknown weapong";
	}

	@Override
	public void setweapon(int weapon) {
		this.weapon = weapon;

	}

	@Override
	public void setSpecial(String special) {
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
		return damge.nextInt(40) + 1;
	}

	@Override
	public void setname(String name) {
		// TODO Auto-generated method stub

	}

	public void setWeapon2012(int w) {
		super.weapon = w;
	}

	@Override
	public String toString() {
		return "Pamintean [fiction=" + fiction + ", name=" + name + ", weapon="
				+ weapon + ", special=" + special + ", getWeapon()="
				+ getWeapon() + ", doHarm()=" + doHarm() + "]";
	}
}
