from animals import *

class Burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu =jenis_bulu
        self.bunyi =bunyi 

    def cetak_Burung(self): 
        super().cetak()
        print(f'Hewan Ini Berbulu {self.jenis_bulu} Dan Hewan Ini Berbunyi {self.bunyi}')

print('----- cetak burung -----')
print('----- objek pertama -----')
beo = Burung('Burung beo', 'Biji -bijian', 'Udara', 'Bertelur', 'Blue Dan Orange', 'Kamu Jelek')
beo.cetak_Burung()

#objek kedua 
print('\n----- objek kedua -----')
merpati = Burung('Burung Merpati', 'Jagung', 'Udara', 'Bertelur', 'Putih', 'Cuaks')
merpati.cetak_Burung()