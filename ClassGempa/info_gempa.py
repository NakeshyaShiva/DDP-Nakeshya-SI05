from Gempa import *

# Membuat Objek Gempa dengan Lokasi dan Skala 
gempa1 = Gempa('Banten', 1.2)
gempa2 = Gempa('Palu', 6.1)
gempa3 = Gempa('Cianjur', 5.6)
gempa4 = Gempa('Jayapura', 3.3)
gempa5 = Gempa('Garut', 4.0)



# Info Gempa 
print('## Gempa Bumi Info Maseh ##')
print()
gempa1.dampak() # Memanggil Method Dampak()

print()
print('## Gempa Bumi Info Maseh ##')
print()
gempa2.dampak() # Memanggil Method Dampak()

print()
print('## Gempa Bumi Info Maseh ##')
print()
gempa3.dampak() # Memanggil Method Dampak()

print()
print('## Gempa Bumi Info Maseh ##')
print()
gempa4.dampak() # Memanggil Method Dampak()

print()
print('## Gempa Bumi Info Maseh ##')
print()
gempa5.dampak() # Memanggil Method Dampak()

