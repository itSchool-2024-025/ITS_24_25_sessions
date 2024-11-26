class Weapon:
    def __init__(self, damage, critical, hit_rate):
        self.damage = damage
        self.critical = critical
        self.hit_rate = hit_rate

class DefenseWeapon:
    pass

class Sword(Weapon):
    def __init__(self, damage, critical, hit_rate, honed):
        super().__init__(damage, critical, hit_rate)
        self.honed = honed

class Shield(DefenseWeapon):
    pass

class Character:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

class Warrior(Character):
    def __init__(self, name, level, weapon: Weapon):
        super().__init__(weapon)
        self.name = name
        self.level = level

if __name__ == "__main__":
    enchanted_sword = Sword("1d4", 0.14, 0.6, True)
    warrior_char = Warrior("fluffy_unicorn", 1, enchanted_sword)