####Laboratorio sobre Vikingos vs Sajones####
####Jorge Montaño#####

import random

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self,dmg):
        self.health = self.health - dmg


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, dmg):
        self.health = self.health - dmg
        if self.health > 0:
            return '{} has received {} points of damage'.format(self.name, dmg)
        else:
           return '{} has died in act of combat'.format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, dmg):
        self.health = self.health - dmg
        if self.health > 0:
            return 'A Saxon has received {} points of damage'.format(dmg)
        else:
           return 'A Saxon has died in combat'


class War:
    def __init__(self): 
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        S = random.choice(self.saxonArmy)
        V = random.choice(self.vikingArmy)
        S.receiveDamage(V.strength)
        if S.health <= 0:
            self.saxonArmy.remove(S)
            return "A Saxon has died in combat"

    
    def saxonAttack(self):
        S = random.choice(self.saxonArmy)
        V = random.choice(self.vikingArmy)
        V.receiveDamage(S.strength)
        if V.health <= 0:
            self.vikingArmy.remove(V)
        else:
            return "{} has received {} points of damage".format(V.name, S.strength)

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
