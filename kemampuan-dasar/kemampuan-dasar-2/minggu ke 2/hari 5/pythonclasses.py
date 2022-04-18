
# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

## CLASS



# class student():
    # nama = 'nama'


    # jumlah_student = 0
    # # jurusan = 'teknik informatika'   # ----> ini variable class
    # # __nilai = 0  #private
    
    # def __init__(self, input_nama, input_nim):    #public
    #     self.nama = input_nama
    #     self.nim = input_nim
    #     student.jumlah_student += 1

    # def uts(self, input_nilai):
    #     self.__nilai += input_nilai
    #     # print(self.nama,'sedang belajar backend', kondisi)

    # def uas(self, input_nilai):
    #     self.__nilai += input_nilai
    #     # print(self.nama,'sedang game mario bross', tidur)  

    # def check_status(self):
    #     if self.__nilai <= 50 :
    #         print(self.nama, 'Tidak Lulus')
    #     else:
    #         print(self.nama, 'Lulus')


## MAIN PROGRAM

# donie = student()
# syafak = student()
# aji = student()
# ikeadely = student()

# donie.nama = 'donie umbara'
# syafak.nama = 'musyafak'
# aji.nama = 'aji pangestu'
# ikeadely.nama = 'game over ikea'

# donie.sinau('python')
# syafak.sinau('javascripts')
# aji.dolanan('menangan')
# ikeadely.dolanan('kalahan')

# donie = student('donie umbara', '123456')
# # donie.sinau('python')
# syafak = student('musyafak', '123455')
# aji = student('aji pangestu', '123454')
# ikeadely = student('ikeadely Ngatukan', '123453')
# # syafak.sinau('javascripts')
# aji = student('aji pangestu', '90')
# aji.dolanan('menangan')

# print(donie.nama)
# print(donie.score)
# print(syafak.nama)
# print(syafak.score)

# donie.uts(20)
# donie.uas(40)
# donie.check_status()
# syafak.uts(30)
# syafak.uas(10)
# syafak.check_status()

# student.jurusan = 'Teknik Informatika Multimedia'
# donie.jurusan = 'Teknik Informatika Multimedia'   # -----> ini variable instance (bagian dari class) kemudian melakukan overwrite di varible class
# donie.kegemaran = 'makan'  # bisa melakukan definisi secara langsung


# print(student.jumlah_student)
# print(donie.jurusan)
# print(syafak.jurusan)
# print(student.jurusan)
# print(student.__dict__)
# print(donie.__dict__)
# print(donie.kegemaran)
# print(donie.__nilai)

# print(donie.nama)
# print(syafak.nama)
# print(aji.nama)
# print(ikeadely.nama)

## INHERITAGE

# class Ojek():

#     def __init__(self, nama, transmisi, daerah):
#         self.nama = nama
#         self.transmisi = transmisi
#         self.daerah = daerah

#     def cek_id_driver(self):
#         print('nama:', self.nama,'\nmotor:',self.transmisi, '\ndaerah:',self.daerah)

# class Grab(Ojek):
    
#     def cek_id_driver(self):
#         print('cek aplikasi GRAB')

# Ojek1 = Ojek('Bambang', 'manual', 'Yogyakarta')
# Ojek2 = Grab('Samsul', 'automatic', 'Bantul')

# Ojek1.cek_id_driver()
# Ojek2.cek_id_driver()

##  TUGAS YANG ADA DI WEBSITE

# menyembunyikan data(data hiding)

# class Counter:
#     __secret_count = 0
    
#     def count(self):
#         self.__secret_count += 1
#         print(self.__secret_count)

# counter = Counter()
# counter.count()
# counter.count()
# print(counter.__secret_count)

# class praxis:
#     tricks = []           

#     def __init__ (self, name):
#         self.name = name

#     def add_trick(self, trick):
#         self.tricks.append(trick)
# d = praxis('donie')
# e = praxis('umbara')
# d.add_trick('roll over')
# e.add_trick('play dead')
# print(d.tricks)


# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'

# def __init__(self):
#     self.data = []

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0, -4.5)
# x.r, x.i
# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter

# class Dog:
    
#     kind = 'canine'         # class variable shared by all instances

#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance

# d = Dog('Fido')
# e = Dog('Buddy')
# print(d.kind)                  # shared by all dogs
# print('e.kind')
# print(d.name)
# print(e.name)

# class Praxis:
#         purpose = 'storage'
#         region = 'west'

# w1 = Praxis()
# print(w1.purpose, w1.region)

# w2 = Praxis()
# w2.region = 'east'
# print(w2.purpose, w2.region)

class praxis:
    '''Dasar kelas untuk semua praxis'''
    jumlah_praxis = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        praxis.jumlah_praxis += 1

    def tampilkan_jumlah(self):
        print("Total praxis:", praxis.praxis)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)

# Membuat objek pertama dari kelas praxiss
praxis1 = praxis("doni", 1000000)
# Membuat objek kedua dari kelas praxis
praxis2 = praxis("syafak", 5000000)

praxis1.tampilkan_profil()
praxis2.tampilkan_profil()
print("Total praxis :", praxis.jumlah_praxis)

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)

print(sum(i*i for i in range(10))) 
syafak = [10, 20, 30]
doni = [7, 5, 3]
print(sum(x*y for x,y in zip(syafak, doni))) 

# unique_words = set('kata demi baris di halaman demi kata di baris'.split())
# pidato perpisahan = max((student.gpa, student.name) untuk mahasiswa di lulusan))

data = 'kafays'

print(list(data[i] for i in range(len(data)-1, -1, -1)))

