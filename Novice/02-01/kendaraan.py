#property adalaha ciri-ciri atau hal-hal yang dimiliki.
#method : kemampuan, tugas atau aktivitas yang dapat dilakukan
#kelas = bentuk abstark dari suatu grub
#contructor = suatu fungsi dari _init_ untuk memberi nilai properti dan dijalankan duluan dari yang lainnya jikalau tidak ada object maka init tidak bisa dijalankan
# inheritance = suatu fungsi pewaris yang mana di dalam class terdaopat ter

#property
class Kendaraan : #kendaraan  punya apa saja
    kecepatan = 0
    cc = 0

#constructor
    def _init_(self):
        self.roda = 0

    def nyala(self): #kendaraan bisa apa ?
        print('brumbrum')

    def maju(self) :
        if self.roda > 0:
            self.kecepatan = self.kecepatan +10

    def mundur(self) :
        pass

#inheritance(pewaris)
class Motor(Kendaraan):
    pass

m1= Motor()
m1.nyala()
m1.roda = 3
print(m1.roda)