import math 

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'Luas Balok adalah {hitung}')

def l_kubus(s):
    hitung = 6 * (s*s)
    print(f'Luas Kubus Adalah {hitung}')

def l_tabung(r, t):
    hitung  = 3.14 * r * r * t 
    print(f'Luas Tabung Adalah {hitung}')

def l_limas(alas, tinggi):
    hitung = 1/2 * alas * tinggi 
    print(f'Luas Limas Segitiga adalah {hitung}')

def l_prisma(l, k, t, a):
    hitung = 2 * 1/2 * a * t + (k * t)
    print(f'Luas Prisma Segitiga adalah {hitung}')