#Soal No 1
print("Soal No 1")
jadwal_hari= ('senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu')
print("Jadwal hari:", jadwal_hari)
print("Tipe data:", type(jadwal_hari))

#Soal No 2
print("Soal No 2")
koordinat = (10, 20, 30, 40, 50)
print("Koordinat:", koordinat)
print("Elemen ke-3:", koordinat[2])
print("Elemen ke-4 dan 5:", koordinat[3:5])

#Soal No 3
print("Soal No 3")
warna = ('merah', 'kuning', 'hijau')
print("Warna sebelum diubah:", warna)
try:  #biar pas error masih bisa lanjut ke kode selanjutnya
    warna[0] = 'ungu'
except TypeError as e:
    print("Terjadi error:", e)
warna = list(warna) #dicasting ke list biar bisa diubah
warna[0] = 'ungu'
warna = tuple(warna)
print("Warna setelah diubah:", warna)

#Soal No 4
print("Soal No 4")
kumpulan_huruf = ('a', 'b', 'c', 'a','d', 'a', 'e')
print("Index dari 'd':", kumpulan_huruf.index('d'))
print("Jumlah kemunculan 'a':", kumpulan_huruf.count('a'))

#Soal No 5
print("Soal No 5")
titik_lokasi = (112.79, -7.28)
longitude = titik_lokasi[0]
latitude = titik_lokasi[1]
print("Longitude:", longitude)
print("Latitude:", latitude)

#Soal No 6
print("Soal No 6")
kendaraan = ('Motor', 'Mobil', 'Sepeda')
print("Kendaraan sebelum diubah:", kendaraan)
kendaraan = list(kendaraan)
kendaraan[1] = 'Bus'
kendaraan = tuple(kendaraan)
print("Kendaraan setelah diubah:", kendaraan)