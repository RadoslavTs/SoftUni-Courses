class Weapon:
    bullets = 0

    def __init__(self, bullets):
        self.bullets = bullets
        Weapon.bullets = self.bullets

    def shoot(self):
        result = ""
        if Weapon.bullets > 0:
            Weapon.bullets -= 1
            result += "shooting..."
        else:
            result += "no bullets left"
        return result

    def __repr__(self):
        return f"Remaining bullets: {Weapon.bullets}"

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
