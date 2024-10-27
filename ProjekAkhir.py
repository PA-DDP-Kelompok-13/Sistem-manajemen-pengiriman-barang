# Data Penyimpanan
pengiriman_list = []
users = {"admin": "admin123"}
current_role = None

# Fungsi untuk Mendaftar Customer
def register_customer():
    username = input("Masukkan username baru: ")
    if username in users:
        print("Username sudah terdaftar. Silakan gunakan username lain.")
        return
    password = input("Masukkan password: ")
    password_confirm = input("Konfirmasi password: ")
    if password != password_confirm:
        print("Password tidak sesuai. Silakan coba lagi.")
        return
    users[username] = password
    print("Pendaftaran berhasil. Silakan login.")

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
    print("Pengiriman berhasil ditambahkan.")

def lihat_pengiriman():
    if not pengiriman_list:
        print("Tidak ada data pengiriman.")
        return
    for pengiriman in pengiriman_list:
        print(f"ID Pengiriman: {pengiriman['id']}, Barang: {pengiriman['barang']}, Tujuan: {pengiriman['tujuan']}, "
              f"Penerima: {pengiriman['penerima']}, Status: {pengiriman['status']}")

def update_pengiriman():
    if current_role != "Admin":
        print("Akses ditolak: Hanya Admin yang dapat memperbarui pengiriman.")
        return
    id_pengiriman = input("ID Pengiriman yang akan diupdate: ")
    for pengiriman in pengiriman_list:
        if pengiriman['id'] == id_pengiriman:
            status = input("Status baru: ")
            pengiriman['status'] = status
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
    print("Pengiriman berhasil dihapus.")

# Fungsi Tracking Pengiriman (Hanya untuk Customer)
def tracking_pengiriman():
    if current_role != "Customer":
        print("Akses ditolak: Hanya Customer yang dapat melakukan tracking pengiriman.")
        return
    id_pengiriman = input("ID Pengiriman yang ingin dilacak: ")
    for pengiriman in pengiriman_list:
        if pengiriman['id'] == id_pengiriman:
            print(f"ID Pengiriman: {pengiriman['id']}, Barang: {pengiriman['barang']}, Tujuan: {pengiriman['tujuan']}, "
                  f"Penerima: {pengiriman['penerima']}, Status: {pengiriman['status']}")
            return
    print("Pengiriman tidak ditemukan.")

# Program Utama
while True:
    print("=== Sistem Manajemen Pengiriman Barang ===")
    print("1. Login sebagai Admin")
    print("2. Pendaftaran Customer")
    print("3. Keluar")

    choice = input("Pilih opsi: ")
    if choice == "1":
        username = "admin"
        password = input("Password: ")
        if login(username, password):
            while True:
                print("\n=== Menu Admin ===")
                print("1. Tambah Pengiriman")
                print("2. Lihat Pengiriman")
                print("3. Update Status Pengiriman")
                print("4. Hapus Pengiriman")
                print("5. Logout")

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
        register_customer()
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if login(username, password):
            while True:
                print("\n=== Menu Customer ===")
                print("1. Tracking Pengiriman")
                print("2. Logout")

                customer_choice = input("Pilih opsi: ")
                if customer_choice == "1":
                    tracking_pengiriman()
                elif customer_choice == "2":
                    print("Logout berhasil.")
                    break
                else:
                    print("Opsi tidak valid. Coba lagi.")

    elif choice == "3":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Opsi tidak valid. Coba lagi.")
