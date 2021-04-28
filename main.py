from AK47 import AK47
from Knife import Knife
from Weapon import Weapon

if __name__ == '__main__':
    weapon = Weapon()

    weapon.set_weapon(Knife())
    weapon.to_apply_weapon()

    weapon.set_weapon(AK47())
    weapon.to_apply_weapon()
