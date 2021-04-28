from IWeapon import IWeapon


class Weapon:

    def __init__(self):
        self.__weapon = IWeapon()

    def set_weapon(self, weapon: IWeapon):
        self.__weapon = weapon

    def to_apply_weapon(self):
        return self.__weapon.to_apply()
