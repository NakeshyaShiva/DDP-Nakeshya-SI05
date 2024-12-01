import math

def l_persegi(sisi):
    luas = sisi * sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas Persegi {sisi} * {sisi} = {luas} ')
    print(f' Keliling Persegi adalah {keliling} ')

def l_lingkaran(jari_jari):
    luas = math.pi * (jari_jari**2)
    print(f'Luas Lingkaran {jari_jari} * {jari_jari} = {luas} ')

def l_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f'Luas Persegi Panjang', panjang, 'x', lebar, '=', luas)

def l_jajargenjang(alas, tinggi):
    luas = alas * tinggi
    print(f'Luas Jajargenjang {alas} * {tinggi} = {luas} ')