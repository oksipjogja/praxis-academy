class Octagram:
    # private class variable
    __jumlah = 0;

    def __init__(self,name):
        self.__name = name
        Octagram.__jumlah += 1
    
    # method yang hanya merubah object
    def getJumlah(self):
        return Octagram.__jumlah
    
    # method ini tidak berlaku pada object tapi berlaku untuk class
    def getJumlah1():
        return Octagram.__jumlah
        
    # method static (decorator) nempel ke object dan class
    @staticmethod
    def getJumlah2():
        return Octagram.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
guy = Octagram('Guy Crimson')
print(Octagram.getJumlah2())
milim = Octagram('Milim Nava')
print(guy.getJumlah2())
ramiris = Octagram('Ramiris')   
print(Octagram.getJumlah3())

# print(Octagram.getJumlah())

