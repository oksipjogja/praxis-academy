class DemonGod:

    def __init__(self,name,mana,magic,barrier):
        self.name = name
        self.mana = mana
        self.magic = magic
        self.barrier = barrier

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)    
        lawan.diserang(self, self.magic)

    def diserang(self, lawan, magic_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = magic_lawan/self.barrier
        print('serangan terasa : ' + str(attack_diterima))
        self.mana -= attack_diterima
        print('darah ' + self.name + ' tersisa ' +str(self.mana))

rimuru = DemonGod('rimuru',1000,100,50)
claymant = DemonGod('claymant',100,20,10)

rimuru.serang(claymant)
print('\n')
claymant.serang(rimuru)
print('\n')
claymant.serang(rimuru)
print('\n')
claymant.serang(rimuru)
print('\n')
claymant.serang(rimuru)
print('\n')
claymant.serang(rimuru)
print('\n')
claymant.serang(rimuru)
print('\n')
claymant.serang(rimuru)
