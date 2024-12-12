from animals import * 

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan
    def cetak_ikan(self):
        super().cetak()
        print(f'Warna Ikan Ini Adalah {self.warna_ikan} Dan Hewan Ini Jenisnya Ikan {self.jenis_ikan}')

print('----- cetak ikan -----')
print('----- objek pertama -----')
Nemo = ikan('Ikan Nemo', 'Plankton', 'Air', 'Bertelur', 'Orange', 'Air Laut')
Nemo.cetak_ikan()

#objek kedua 
print('\n----- objek kedua -----')
Lele = ikan('Ikan Lele', 'Ikan Runcah', 'Air', 'Bertelur', 'Hitam', 'Airbreathing catfish ')
Lele.cetak_ikan()

