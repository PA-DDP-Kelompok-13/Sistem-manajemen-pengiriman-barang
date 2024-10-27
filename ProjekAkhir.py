# Data Penyimpanan
pengiriman_list = []
users = {"admin": "admin123", "customer": "customer123"}
current_role = None

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
print("Silakan Login")
username = input("Username: ")
password = input("Password: ")

if login(username, password):
    while True:
        if current_role == "Admin":
            print("\n=== Menu Admin ===")
            print("1. Tambah Pengiriman")
            print("2. Lihat Pengiriman")
            print("3. Update Status Pengiriman")
            print("4. Hapus Pengiriman")
            print("5. Logout")

            choice = input("Pilih opsi: ")
            if choice == "1":
                tambah_pengiriman()
            elif choice == "2":
                lihat_pengiriman()
            elif choice == "3":
                update_pengiriman()
            elif choice == "4":
                hapus_pengiriman()
            elif choice == "5":
                print("Logout berhasil.")
                break
            else:
                print("Opsi tidak valid. Coba lagi.")

        elif current_role == "Customer":
            print("\n=== Menu Customer ===")
            print("1. Tracking Pengiriman")
            print("2. Logout")

            choice = input("Pilih opsi: ")
            if choice == "1":
                tracking_pengiriman()
            elif choice == "2":
                print("Logout berhasil.")
                break
            else:
                print("Opsi tidak valid. Coba lagi.")
else:
    print("Login gagal.")
