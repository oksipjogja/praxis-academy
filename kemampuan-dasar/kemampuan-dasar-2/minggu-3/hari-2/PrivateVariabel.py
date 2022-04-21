class DemonGod:
    # class variable
    jumlah = 0
    __privateJumlah = 0
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana

        # variable instance private
        self.__private = "private"
        # variable instace protected
        self._protected = "protected"

        
rimuru = DemonGod("Rimuru Tempest", 1000)

print(rimuru.__dict__)
print(DemonGod.__dict__)


# print(DemonGod.__privateJumlah)  # di private menyebabkan error
# print(rimuru._protected)
# print(rimuru._protected)
# rimuru._protected = "diablo"
# print(rimuru.__dict__)
# # print(rimuru.private)
# print(rimuru.mana)
# rimuru.private = "slime"
    
      
