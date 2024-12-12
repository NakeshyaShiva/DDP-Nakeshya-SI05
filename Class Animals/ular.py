from animals import * 

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ular = warna_ular
        self.jenis_ular = jenis_ular 

    def cetak_ular(self):
        super().cetak()
        print(f'Warna Ular Ini Adalah {self.warna_ular} Dan Hewan Ini Jenisnya ular {self.jenis_ular}')

print('----- cetak ular -----')
print('----- objek pertama -----')
Kukri_trioman = ular('Ular Kukri Trioman', 'Burung', 'Tanah', 'Bertelur', 'Coklat', 'Berbisa' )
Kukri_trioman.cetak_ular()

#objek kedua 
print('\n----- objek kedua -----')
Sanca = ular('Ular Sanca', 'Reptil', 'Darat', 'Bertelur', 'Kecoklatan', 'Tidak Berbisa')
Sanca.cetak_ular()

