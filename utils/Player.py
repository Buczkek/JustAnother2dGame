from Object import Object
from Inventory import Inventory


class Player(Object):  # TODO Player class
    def __init__(self):
        super().__init__()
        self._Health = 100
        self._Armor = 0
        self._MaxHealth = 100
        self._MaxArmor = 100
        self._Dead = False
        self._Inventory = Inventory()
        self._MoveAble = True

    def IsDead(self):
        return self._Dead

    def IsAlive(self):
        return not self._Dead

    def GetHealth(self):
        return self._Health

    def GetArmor(self):
        return self._Armor

    def DealDamage(self, Damage: int, IgnoreArmor: bool):
        if not IgnoreArmor:
            if Damage <= self._Armor:
                self._Armor -= Damage
                return False
            else:
                Damage -= self._Armor
                self._Armor = 0
        self._Health -= Damage
        if self._Health < 0:
            self.Kill()

    def Kill(self):
        self._Dead = True

    def Heal(self, heal):
        self._Health = self._MaxHealth if (self._Health + heal) > self._MaxHealth else self._Health + heal

    # TODO ...
