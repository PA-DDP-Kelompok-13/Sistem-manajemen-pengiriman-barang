from prettytable import PrettyTable
import pwinput
import csv
import os

# Data Penyimpanan
pengiriman_list = []
users = {"admin": "admin123"}
current_role = None
csv_file = "datapengiriman.csv"

# Fungsi untuk memuat data dari file CSV
def load_data_from_csv():
    if os.path.exists(csv_file):
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pengiriman_list.append(row)

# Fungsi untuk menyimpan data ke file CSV
def save_data_to_csv():
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ["id", "barang", "tujuan", "penerima", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(pengiriman_list)

# Load data dari CSV saat program dimulai
load_data_from_csv()

# Fungsi untuk Mendaftar Customer
def register_customer():
    username = input("Masukkan username baru: ")
    if username in users: 
        print("Username sudah terdaftar. Silakan gunakan menu login.")
        return False
    password = pwinput.pwinput("Masukkan password: ")
    password_confirm = pwinput.pwinput("Konfirmasi password: ")
    if password != password_confirm:
        print("Password tidak sesuai. Silakan coba lagi.")
        return False
    users[username] = password
    print("Pendaftaran berhasil.")
    return True

# Fungsi Login
def login(username, password):
    global current_role
    if username in users and users[username] == password:
        current_role = "Admin" if username == "admin" else "Customer"
        print(f"Login berhasil sebagai {current_role}")
        return True
    else:
        print("Username atau password salah")
        return False

# Fungsi CRUD Pengiriman (Hanya untuk Admin)
def tambah_pengiriman():
    if current_role != "Admin":
        print("Akses ditolak: Hanya Admin yang dapat menambahkan pengiriman.")
        return
    id_pengiriman = input("ID Pengiriman: ")
    barang = input("Nama Barang: ")
    tujuan = input("Tujuan Pengiriman: ")
    penerima = input("Nama Penerima: ")
    status = "Dalam Proses"
    pengiriman = {"id": id_pengiriman, "barang": barang, "tujuan": tujuan, "penerima": penerima, "status": status}
    pengiriman_list.append(pengiriman)
    save_data_to_csv()
    print("Pengiriman berhasil ditambahkan.")

def lihat_pengiriman():
    if not pengiriman_list:
        print("Tidak ada data pengiriman.")
        return
    table = PrettyTable()
    table.field_names = ["ID Pengiriman", "Nama Barang", "Tujuan", "Nama Penerima", "Status"]
    for pengiriman in pengiriman_list:
        table.add_row([pengiriman["id"], pengiriman["barang"], pengiriman["tujuan"], pengiriman["penerima"], pengiriman["status"]])
    print(table)

def update_pengiriman():
    if current_role != "Admin":
        print("Akses ditolak: Hanya Admin yang dapat memperbarui pengiriman.")
        return
    id_pengiriman = input("ID Pengiriman yang akan diupdate: ")
    for pengiriman in pengiriman_list:
        if pengiriman['id'] == id_pengiriman:
            status = input("Status baru: ")
            pengiriman['status'] = status
            save_data_to_csv()
            print("Status pengiriman berhasil diperbarui.")
            return
    print("Pengiriman tidak ditemukan.")

def hapus_pengiriman():
    if current_role != "Admin":
        print("Akses ditolak: Hanya Admin yang dapat menghapus pengiriman.")
        return
    id_pengiriman = input("ID Pengiriman yang akan dihapus: ")
    global pengiriman_list
    pengiriman_list = [p for p in pengiriman_list if p['id'] != id_pengiriman]
    save_data_to_csv()
    print("Pengiriman berhasil dihapus.")

# Fungsi Tracking Pengiriman (Hanya untuk Customer)
def tracking_pengiriman():
    if current_role != "Customer":
        print("Akses ditolak: Hanya Customer yang dapat melakukan tracking pengiriman.")
        return
    id_pengiriman = input("ID Pengiriman yang ingin dilacak: ")
    for pengiriman in pengiriman_list:
        if pengiriman['id'] == id_pengiriman:
            table = PrettyTable()
            table.field_names = ["ID Pengiriman", "Nama Barang", "Tujuan", "Nama Penerima", "Status"]
            table.add_row([pengiriman["id"], pengiriman["barang"], pengiriman["tujuan"], pengiriman["penerima"], pengiriman["status"]])
            print(table)
            return
    print("Pengiriman tidak ditemukan.")

# Fungsi Menampilkan Informasi Customer Service
def customer_service():
    table = PrettyTable()
    table.field_names = ["Kontak", "Informasi"]
    table.add_row(["Nomor WhatsApp", "085754752258"])
    table.add_row(["Email", "ayarighen@gmail.com"])
    print("\n=== Customer Service ===")
    print(table)

# Fungsi Tampilan Menu dengan PrettyTable
def tampilkan_menu(role):
    table = PrettyTable()
    if role == "Admin":
        table.field_names = ["No", "Opsi Menu Admin"]
        table.add_row(["1", "Tambah Pengiriman"])
        table.add_row(["2", "Lihat Pengiriman"])
        table.add_row(["3", "Update Status Pengiriman"])
        table.add_row(["4", "Hapus Pengiriman"])
        table.add_row(["5", "Logout"])
    elif role == "Customer":
        table.field_names = ["No", "Opsi Menu Customer"]
        table.add_row(["1", "Tracking Pengiriman"])
        table.add_row(["2", "Customer Service"])
        table.add_row(["3", "Logout"])
    print(table)

# Fungsi Menu Utama dengan PrettyTable
def tampilkan_menu_utama():
    table = PrettyTable()
    table.field_names = ["No", "Pilihan Utama"]
    table.add_row(["1", "Login sebagai Admin"])
    table.add_row(["2", "Pendaftaran Customer"])
    table.add_row(["3", "Login sebagai Customer"])
    table.add_row(["4", "Keluar"])
    print(table)

# Program Utama
while True:
    print("=== Sistem Manajemen Pengiriman Barang ===")
    tampilkan_menu_utama()

    choice = input("Pilih opsi: ")
    if choice == "1":
        username = "admin"
        password = pwinput.pwinput("Password: ")
        if login(username, password):
            while True:
                print("\n=== Menu Admin ===")
                tampilkan_menu("Admin")
                admin_choice = input("Pilih opsi: ")
                if admin_choice == "1":
                    tambah_pengiriman()
                elif admin_choice == "2":
                    lihat_pengiriman()
                elif admin_choice == "3":
                    update_pengiriman()
                elif admin_choice == "4":
                    hapus_pengiriman()
                elif admin_choice == "5":
                    print("Logout berhasil.")
                    break
                else:
                    print("Opsi tidak valid. Coba lagi.")

    elif choice == "2":
        if register_customer():
            print("Pendaftaran berhasil. Silakan login sebagai customer.")

    elif choice == "3":
        username = input("Masukkan username untuk login: ")
        password = pwinput.pwinput("Masukkan password untuk login: ")
        if login(username, password):
            while True:
                print("\n=== Menu Customer ===")
                tampilkan_menu("Customer")
                customer_choice = input("Pilih opsi: ")
                if customer_choice == "1":
                    tracking_pengiriman()
                elif customer_choice == "2":
                    customer_service()
                elif customer_choice == "3":
                    print("Logout berhasil.")
                    break
                else:
                    print("Opsi tidak valid. Coba lagi.")

    elif choice == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Opsi tidak valid. Coba lagi.")
