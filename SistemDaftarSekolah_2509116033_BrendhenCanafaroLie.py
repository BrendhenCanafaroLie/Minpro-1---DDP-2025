

ekskul = [("Basket", "Pak Andi", "Senin & Rabu 15.00"), 
("Paduan Suara", "Bu Sinta", "Selasa 16.00"), 
("Pramuka", "Pak Budi", "Jumat 14.00")]

print("===Daftar Ekstrakurikuler Sekolah ===")
print("----------------------------------------------")
print("1. Tambah Ekstrakurikuler")
print("2. Lihat Daftar Ekstrakurikuler")
print("3. Ubah Data Ekstrakurikuler")
print("4. Hapus Ekstrakurikuler")
print("5. Keluar")
print("----------------------------------------------")

data = int(input("Masukkan Nomor Pilihan : "))

if data == 1:
    nama = input("Masukkan nama ekskul: ")
    pembina = input("Masukkan nama pembina: ")
    jadwal = input("Masukkan jadwal: ")
    ekskul.append((nama, pembina, jadwal))
    print(" Ekstrakurikuler berhasil ditambahkan!")
elif data == 2:
    if ekskul:
        print("Berikut Daftar Estrakurikuler")
        print(ekskul)
    else:
        print("Tidak Ada Data Ekskul")
elif data == 3:
    print(ekskul)
    ubah = int(input("Pilih nomor ekskul yang ingin diubah : ")) - 1
    print("Sekarang Masukkan Ekskul baru yang ingin digantikan")
    nama = input("Masukkan nama ekskul: ")
    pembina = input("Masukkan nama pembina: ")
    jadwal = input("Masukkan jadwal: ")
    
    ekskul[ubah] = (nama, pembina, jadwal)
    print("Anda Berhasil Mengubah Ekskul")
elif data == 4:
    print(ekskul)
    ubah = int(input("Pilih nomor ekskul yang ingin diubah : ")) - 1
    del ekskul[ubah]
    print("Anda Berhasil Menghapus Ekskul")
elif data == 5:
    print("Terima Kasih *PROGRAM BERAKHIR")
else:
    print("NOMOR INVALID")



