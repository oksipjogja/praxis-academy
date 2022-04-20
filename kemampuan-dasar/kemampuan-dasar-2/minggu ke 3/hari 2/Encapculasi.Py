class DemonGod :

    def __init__(self,name,mana,attackPower):
        self.__name = name
        self.__mana = mana
        self.__attPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getMana(self):
        return self.__mana

    # setter
    def cure(self, curePower):
        self.__mana -= curePower


# awal anime
rimuru = DemonGod('Rimuru Tempest', 1000, 100000)

# anime berjalan

print(rimuru.getName())
print(rimuru.getMana())
rimuru.cure(100)
print(rimuru.getMana())



# print(rimuru.__dict__)
""" encapculasi --> membuat private semua variabel
dan untuk mengeksekusinya menggunakan getter (mengambil variabel) 
dan setter (untuk mensetting variabel)""" 