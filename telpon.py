# Buku Telepon Sederhana

# Data kontak awal disimpan dalam dictionary
kontak = {
    "Andi": "08123456789",
    "Budi": "08234567890",
    "Citra": "08345678901"
}

def tampilkan_kontak():
    print("\nDaftar Kontak:")
    # Mengurutkan nama kontak dan menampilkan nomor
    for nama in sorted(kontak.keys()):
        print(f"{nama}: {kontak[nama]}")

def cari_kontak():
    nama_cari = input("\nMasukkan nama yang ingin dicari: ").strip()
    # Membuat pencarian tidak case sensitive
    nama_cari_lower = nama_cari.lower()

    ditemukan = False
    for nama in kontak:
        if nama.lower() == nama_cari_lower:
            print(f"Nomor telepon {nama}: {kontak[nama]}")
            ditemukan = True
            break
    if not ditemukan:
        print("Kontak tidak ditemukan.")

def tambah_kontak():
    nama_baru = input("\nMasukkan nama kontak baru: ").strip()
    nomor_baru = input("Masukkan nomor telepon: ").strip()
    kontak[nama_baru] = nomor_baru
    print(f"Kontak {nama_baru} berhasil ditambahkan.")

# Program utama
while True:
    print("\nMenu Buku Telepon")
    print("1. Tampilkan Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ").strip()

    if pilihan == "1":
        tampilkan_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
