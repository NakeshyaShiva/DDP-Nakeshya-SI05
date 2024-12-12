class animal: 
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama 
        self.makanan = makanan 
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak 

    def cetak(self):
        print(f'Hewan {self.nama} Ini Memakan {self.makanan} Hewan Ini Juga Hidup Di {self.hidup} Dan Berkembang Biak Dengan Cara {self.berkembang_biak}')

c1 = animal('Buaya', 'Daging', 'Amphibi', 'Bertelur')
c1.cetak()