# class Hero:     # template
#     pass
# hero1 = Hero()   # object / instance (proses : instansiate)
# hero2 = Hero()
# hero3 = Hero()

# hero1.name = 'sniper'
# hero1.health = 100

# hero2.name = 'sven'
# hero2.health = 200

# hero3.name = 'ucup'
# hero3.health = 1000

# print(hero1)
# print(hero1.__dict__)
# print(hero1.name)

class Hero:  
    # class varible
    jumlah_hero = 0  
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance Variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
        # print('membuat Hero dengan nama ' + inputName)

    # void function, method tanpa return tanpa argumen
    def siapa(self):
        print('namaku adalah ' + self.name)
    
    # method dengan argumen tanpa return
    def healthUp(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health



hero1 = Hero('sniper', 100,10,5)
# print(Hero.jumlah)
hero2 = Hero('mario bros',90,5,10)
# print(Hero.jumlah)
# hero3 = Hero('ucup',1000,100,0)
# print(Hero.jumlah)
# print(hero1.__dict__)
# print(hero2.__dict__)
hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())


# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)
# print(Hero.__dict__)

print(hero1.__dict__)