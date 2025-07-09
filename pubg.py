import csv
from datetime import datetime

# Nama file CSV
nama_file = 'transaksi_pubg.csv'

# Inisialisasi file jika belum ada
def inisialisasi_file():
    try:
        with open(nama_file, mode='x', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Nama", "ID PUBG", "Jumlah UC", "Harga", "Tanggal"])
            writer.writeheader()
    except FileExistsError:
        pass

# Fitur 1: Top Up UC
def top_up_uc():
    nama = input("Masukkan Nama Anda: ")
    id_pubg = input("Masukkan ID PUBG: ")
    print("Pilih jumlah UC:")
    print("1. 60 UC  - Rp15.000")
    print("2. 325 UC - Rp75.000")
    print("3. 660 UC - Rp150.000")
    
    pilihan = input("Masukkan pilihan (1/2/3): ")

    uc_dict = {
        "1": (60, 15000),
        "2": (325, 75000),
        "3": (660, 150000)
    }

    if pilihan not in uc_dict:
        print(" Pilihan tidak valid!")
        return

    jumlah_uc, harga = uc_dict[pilihan]
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "Nama": nama,
        "ID PUBG": id_pubg,
        "Jumlah UC": jumlah_uc,
        "Harga": harga,
        "Tanggal": tanggal
    }

    with open(nama_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)

    print(" Top Up berhasil!")

# Fitur 2: Lihat Riwayat Transaksi
def lihat_riwayat():
    try:
        with open(nama_file, mode='r') as file:
            reader = csv.DictReader(file)
            transaksi = list(reader)

            if not transaksi:
                print(" Belum ada transaksi.")
                return

            print("\n📋 Riwayat Transaksi:")
            for idx, row in enumerate(transaksi, start=1):
                print(f"{idx}. {row['Nama']} - ID: {row['ID PUBG']}, UC: {row['Jumlah UC']}, Harga: Rp{row['Harga']}, Tanggal: {row['Tanggal']}")
    except FileNotFoundError:
        print(" File tidak ditemukan.")

# Fitur 3: Edit Transaksi berdasarkan ID PUBG
def edit_transaksi():
    id_target = input("Masukkan ID PUBG yang ingin diedit: ")
    ditemukan = False

    # Baca semua transaksi
    with open(nama_file, mode='r') as file:
        reader = csv.DictReader(file)
        transaksi = list(reader)

    for i, row in enumerate(transaksi):
        if row['ID PUBG'] == id_target:
            print(f"Transaksi ditemukan: {row}")
            print("Apa yang ingin diubah?")
            print("1. Nama")
            print("2. Jumlah UC")
            pilihan = input("Pilih (1/2): ")

            if pilihan == "1":
                nama_baru = input("Masukkan nama baru: ")
                transaksi[i]['Nama'] = nama_baru
            elif pilihan == "2":
                print("Pilihan UC:")
                print("1. 60 UC  - Rp15.000")
                print("2. 325 UC - Rp75.000")
                print("3. 660 UC - Rp150.000")
                pilih_uc = input("Masukkan pilihan (1/2/3): ")
                uc_dict = {
                    "1": (60, 15000),
                    "2": (325, 75000),
                    "3": (660, 150000)
                }
                if pilih_uc in uc_dict:
                    jumlah_uc, harga = uc_dict[pilih_uc]
                    transaksi[i]['Jumlah UC'] = jumlah_uc
                    transaksi[i]['Harga'] = harga
                    transaksi[i]['Tanggal'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                else:
                    print(" Pilihan UC tidak valid!")
                    return
            else:
                print(" Pilihan tidak valid.")
                return

            ditemukan = True
            break

    if ditemukan:
        with open(nama_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Nama", "ID PUBG", "Jumlah UC", "Harga", "Tanggal"])
            writer.writeheader()
            writer.writerows(transaksi)
        print("✅ Transaksi berhasil diperbarui.")
    else:
        print(" ID PUBG tidak ditemukan.")

# Menu Utama
def menu():
    inisialisasi_file()
    while True:
        print("\n=== SISTEM TOP UP UC PUBG MOBILE ===")
        print("1. Top Up UC")
        print("2. Lihat Riwayat Transaksi")
        print("3. Edit Transaksi (berdasarkan ID PUBG)")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            top_up_uc()
        elif pilihan == "2":
            lihat_riwayat()
        elif pilihan == "3":
            edit_transaksi()
        elif pilihan == "4":
            print("👋 Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print(" Pilihan tidak valid!")

# Jalankan program
menu()
