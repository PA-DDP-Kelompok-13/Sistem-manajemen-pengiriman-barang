from prettytable import PrettyTable
import csv
import pwinput

STATUS_MENUNGGU_PEMBAYARAN = "Menunggu Pembayaran"
STATUS_DALAM_ANTRIAN = "Sedang dalam antrian"
FILE_AKUN_USERS = "Akun_Pengguna.csv"
FILE_DATA_PENGIRIMAN = "All_Data_Pengiriman.csv"

def tampilan_login():
    tablelogin = PrettyTable()

    tablelogin.field_names = ["Opsi", "Login"]

    tablelogin.add_row(["1", "ADMIN"])
    tablelogin.add_row(["2", "CUSTOMER"])
    tablelogin.add_row(["3", "KEMBALI"])

    print(tablelogin)

def registrasi_akun():
    username = input("Buat Username Anda: ")
    password = pwinput.pwinput("Buat Password Anda: ")
    saldo = 0

    with open(FILE_AKUN_USERS, mode="a", newline="") as file:
        Write = csv.writer(file)
        Write.writerow([username, password, saldo])
    print("_Akun Anda Berhasil Dibuat_")

def validasi_akun(username, password):

    with open(FILE_AKUN_USERS, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:

            if row[0] == username and row[1] == password:
                return True
    return False

def validasi_akun_admin(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False

def tampilan_admin():
    tableadmin = PrettyTable()

    tableadmin.field_names = ["Opsi", "Selamat Datang ADMIN"]

    tableadmin.add_row(["1", "Ubah/Update Status Data Pengiriman"])
    tableadmin.add_row(["2", "Hapus Data Pengiriman"])
    tableadmin.add_row(["3", "Lihat Data Pengiriman"])
    tableadmin.add_row(["4", "Cari Data Pengiriman"])
    tableadmin.add_row(["5", "Sorting Data Pengiriman"])
    tableadmin.add_row(["6", "LogOut"])

    print(tableadmin)

def login_admin():
    print("-----Selamat Datang ADMIN-----")

    username = input("Masukkan Username ADMIN: ")
    password = pwinput.pwinput("Masukkan Password ADMIN: ")
    
    if validasi_akun_admin(username, password):
        print("-----Login Berhasil !!!-----")

        while True:

            tampilan_admin()

            opsi_admin = input("Masukkan Opsi Pilihan: ")
            
            if opsi_admin == "1":
                Ubah_Data()
            elif opsi_admin == "2":
                Hapus_Pengiriman()
            elif opsi_admin == "3":
                Lihat_Pengiriman()
            elif opsi_admin == "4":
                Fitur_Cari()
            elif opsi_admin == "5":
                Fitur_Sorting()
            elif opsi_admin == "6":
                print("--LogOut Berhasil!!--")
                break
            else:
                print("Pilihan tidak valid, silahkan anda coba lagi")
    else:
        print("Username atau Password Admin Salah!")

def tampilan_customer():
    tablecus = PrettyTable()

    tablecus.field_names = ["Opsi", "Selamat Datang Customer"]

    tablecus.add_row(["1", "Buat Pengiriman"])
    tablecus.add_row(["2", "Lihat Pengiriman"])
    tablecus.add_row(["3", "TOPUP"])
    tablecus.add_row(["4", "LogOut"])

    print(tablecus)

def login_customer():
    username = input("Masukkan Username Anda: ")
    password = pwinput.pwinput("Masukkan Password Anda: ")

    if validasi_akun(username, password):
        print("--Login Berhasil!--")

        while True:
            
            tampilan_customer()

            opsi_customer = input("Masukkan Opsi Pilihan: ")

            if opsi_customer == "1":
                Buat_Pengiriman(username)
            elif opsi_customer == "2":
                Lihat_Pengiriman_Customer(username)
            elif opsi_customer == "3":
                top_up(username)
            elif opsi_customer == "4":
                print("--LogOut Berhasil!!--")
                break
            else:
                print("Pilihan tidak valid, silahkan anda coba lagi")
    else:
        print("Username atau Password Anda Salah!")

def Buat_Pengiriman(username):
    with open(FILE_DATA_PENGIRIMAN, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data = list(reader)

        if len(data) > 0 and len(data[0]) > 0:
            id_terakhir = int(data[-1][0])
        else:
            id_terakhir = 0

        id_pengiriman = id_terakhir + 1
        nama_barang = input("Masukkan Barang yang ingin di Kirim: ")
        tujuan_pengiriman = input("Masukkan Kota Tujuan Pengiriman: ")
        nama_pengirim = input("Masukkan Nama Pengirim Barang: ")
        nama_penerima = input("Masukkan Nama Penerima Barang: ")
        tanggal_Pengiriman = input("Masukkan Tanggal Pengiriman (Tahun-Bulan-Tanggal): ")
        Status_pengiriman = STATUS_MENUNGGU_PEMBAYARAN

        with open(FILE_DATA_PENGIRIMAN, mode="a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([id_pengiriman, nama_barang, tujuan_pengiriman, nama_pengirim, nama_penerima, tanggal_Pengiriman, Status_pengiriman])

        print(f"{nama_barang} dengan ID {id_pengiriman} berhasil di Tambahka dengan status {Status_pengiriman}")

        pembayaran = input("Apakah anda Ingin melakukan pembayaran untuk pengiriman ini? [y/n]: ").lower()
        
        if pembayaran == "y":
            pembayaran_Pengiriman(username)
        else:
            print("Pengiriman Tertunda Sampai Anda Melakukan Pembayaran")

def tampilan_table(data,headers):
    table = PrettyTable()
    table.field_names = headers
    for row in data:
        print(row)
        table.add_row(row)
    print(table)

def Lihat_Pengiriman():
    table = PrettyTable()
    table.field_names = ["ID", "Nama_Barang", "Kota_Tujuan", "Nama_Pengirim", "Nama_Penerima", "Tanggal_Pengiriman", "Status_Pengiriman"]

    with open(FILE_DATA_PENGIRIMAN, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Melewati header asli dari file CSV

        for row in reader:
            if len(row) == 7:  # Pastikan ada 7 kolom
                table.add_row(row)
            else:
                print("Error: Baris data tidak memiliki 7 kolom:", row)
    
    print(table)

def top_up(username):
    akun = []
    found = False

    # Open the user account file to load data
    with open(FILE_AKUN_USERS, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        akun = list(reader)

    # Search for the user in account data
    for row in akun:
        if row[0] == username:
            password = pwinput.pwinput("Masukkan password Anda: ")
            
            # Validate password
            if row[1] != password:
                print("Password anda salah!.")
                return
            
            try:
                # Input validation for top-up amount
                jumlah_topup = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
                if jumlah_topup <= 0:
                    print("Jumlah saldo harus lebih dari 0!")
                    return

                # Update the user's balance
                row[2] = str(int(row[2]) + jumlah_topup)
                found = True
                print(f"TopUp berhasil! Saldo terbaru: {row[2]}")
            except ValueError:
                print("Jumlah saldo harus berupa angka!")
            break

    if not found:
        print("Username tidak ditemukan.")

    with open(FILE_AKUN_USERS, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(akun)

def Lihat_Pengiriman_Customer(username):
    tablecustomer = PrettyTable()

    tablecustomer.field_names = ["ID", "Nama_Barang", "Kota_Tujuan", "Nama_Pengirim", "Nama_Penerima", "Tanggal_Pengiriman", "Status_Pengiriman"]

    data_found = False
    
    with open(FILE_DATA_PENGIRIMAN, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:

            if row[3] == username:
                tablecustomer.add_row(row)
                data_found = True

    if data_found:
        print("Data Pengiriman Anda: ")
        print(tablecustomer)
    else:
        print("Anda Belum Memiliki Riwayat Pengiriman")

def Ubah_Data():
    Lihat_Pengiriman()

    id_pengiriman = input("Masukkan ID Barang Yang Ingin Di Update Statusnya: ")
    dataupdate = []
    perubahan = False

    with open(FILE_DATA_PENGIRIMAN, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        for row in reader:
            if row[0] == id_pengiriman:
                row[6] = input("Ubah Status Pengiriman: ")
                perubahan = True
            dataupdate.append(row)

    # Jika ada perubahan, tulis ulang ke file CSV
    if perubahan:
        with open(FILE_DATA_PENGIRIMAN, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(dataupdate)
        
        print("Status Data Pengiriman Berhasil Di Update!")
        print("\nData setelah diperbarui:")
        
        # Tampilkan data setelah diperbarui
        table = PrettyTable()
        table.field_names = ["ID", "Nama_Barang", "Kota_Tujuan", "Nama_Pengirim", "Nama_Penerima", "Tanggal_Pengiriman", "Status_Pengiriman"]
        for row in dataupdate:
            if len(row) == 7:
                table.add_row(row)
        
        print(table)
    else:
        print("ID Pengiriman Tidak Dapat Ditemukan!")

def Hapus_Pengiriman():

    Lihat_Pengiriman()

    id_Pengiriman = input("Masukkan ID Pengiriman Yang Ingin di Hapus: ")
    datahapus = []
    terhapus = False

    with open(FILE_DATA_PENGIRIMAN, mode="r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        datahapus.append(header)
        
        for row in reader:
            if row[0] != id_Pengiriman:
                datahapus.append(row)
            else:
                terhapus = True

    if terhapus:
        
        with open(FILE_DATA_PENGIRIMAN, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(datahapus)
            print("Data Pengiriman Berhasil Di Hapus!")
    else:
        print("ID Pengiriman Tidak Dapat Ditemukan!")

def Fitur_Cari():

    Lihat_Pengiriman()

    keyword = input("Masukkan Nama Barang Yang Ingin Di Cari: ")
    pencarian = []

    with open(FILE_DATA_PENGIRIMAN, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            if keyword in row[1]:
                pencarian.append(row)

    if pencarian:
        tampilan_table(pencarian, ["ID", "Nama_Barang", "Kota_Tujuan", "Nama_Pengirim", "Nama_Penerima", "Tanggal_Pengiriman", "Status_Pengiriman"])
    else:
        print("Barang Tidak Ditemukan!")

def Fitur_Sorting():

    Lihat_Pengiriman()

    while True:
        print("1. Urutkan berdasarkan Nama barang")
        print("2. Urutkan berdasarkan Kota Tujuan")
        print("3. Urutkan berdasarkan Tanggal Pengiriman")
        print("4. Kembali ke menu utama")

        urutkan = input("Masukkan Opsi: ")

        if urutkan == "4":
            break

        with open(FILE_DATA_PENGIRIMAN, mode="r") as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

            data = [row for row in data if len(row) == 7 ]
            
            if len(data) > 1:
                header = data[0]
                data = data[1:]
            else:
                print("Data Pengiriman Kosong atau tidak Tersedia!")
                return
            
            if urutkan == "1":
                data.sort(key=lambda x: x[1])
            elif urutkan == "2":
                data.sort(key=lambda x: x[2])
            elif urutkan == "3":
                data.sort(key=lambda x: x[5])
            else:
                print("Tolong Masukkan Sesuai dengan Opsi Yang Ada!")
                continue

            print("List Data Pengiriman Berhasik Di Urutkan!")
            tampilan_table([header] + data, ["ID", "Nama_Barang", "Kota_Tujuan", "Nama_Pengirim", "Nama_Penerima", "Tanggal_Pengiriman", "Status_Pengiriman"])
    
def pembayaran_Pengiriman(username):
    print("Daftar Pengiriman Barang dengan Status Menunggu Pembayaran.")

    with open(FILE_DATA_PENGIRIMAN, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data_pengiriman = list(reader)

        Pembayaran_Tertunda = [row for row in data_pengiriman if len(row) >= 6 and row[-1].lower() == STATUS_MENUNGGU_PEMBAYARAN.lower()]

        if Pembayaran_Tertunda:
            tampilan_table(Pembayaran_Tertunda, ["ID", "Nama_Barang", "Kota_Tujuan", "Nama_Pengirim", "Nama_Penerima", "Tanggal_Pengiriman", "Status_Pengiriman"])
        else:
            print("Tidak Ada Pengiriman Dengan Status 'Menunggu Pembayaran'.")
            return
        
        id_pengiriman = input("Masukkan ID Pengiriman yang Ingin DiBayar: ")
        berat_barang = float(input("Masukkan Berat Barang dengan satuan KiloGram (KG): "))

        if berat_barang <= 3:
            harga = 30000
        elif 3 < berat_barang <= 7:
            harga = 50000
        else:
            harga = 100000

        with open(FILE_AKUN_USERS, mode="r") as csvfile:
            reader = csv.reader(csvfile)
            akun_user = list(reader)

        for akun in akun_user:
            if akun[0] == username:
                saldo = int(akun[2])

                if saldo >= harga:

                    saldo -= harga
                    akun[2] = str(saldo)
                    pembayaran_berhasil = False

                    for row in data_pengiriman:
                        if row[0] == id_pengiriman and row[-1].lower() == STATUS_MENUNGGU_PEMBAYARAN.lower():
                            row[-1] = STATUS_DALAM_ANTRIAN
                            pembayaran_berhasil = True
                            break
                    
                    with open(FILE_AKUN_USERS, mode="w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(akun_user)

                    with open(FILE_DATA_PENGIRIMAN, mode="w", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(["ID", "Nama_Barang", "Kota_Tujuan", "Nama_Pengirim", "Nama_Penerima", "Tanggal_Pengiriman", "Status_Pengiriman"])
                        writer.writerows(data_pengiriman)
    
                    if pembayaran_berhasil:
                        print("Pembayaran Berhasil! Status Pengiriman Di Perbarui menjadi 'Sedang Dalam Antrian'.")
                    else:
                        print("ID Pengiriman Tidak ditemukan atau sudah dibayar!")
                else:
                    print("Saldo Anda tidak cukup untuk pembayaran. Silakan lakukan TopUp terlebih dahulu.")
                return
            
        print("Username tidak ditemukan atau tidak valid.")        

def tampilan_utama():
    while True:
        try:
            # Membuat tampilan utama menggunakan PrettyTable
            tableUtama = PrettyTable()
            tableUtama.field_names = ["Opsi", "SISTEM PENGIRIMAN BARANG"]
            tableUtama.add_row(["1", "Registrasi Akun"])
            tableUtama.add_row(["2", "Login"])
            tableUtama.add_row(["3", "EXIT"])

            print(tableUtama)

            # Menerima input dari user dengan try-except
            opsi = input("Masukkan Pilihan Opsi: ")

            if opsi == "1":
                registrasi_akun()  # Panggil fungsi registrasi akun
            elif opsi == "2":
                tampilan_login()  # Panggil fungsi login
                
                pilihan_role = input("Masukkan Pilihan Role Anda: ")
                
                if pilihan_role == "1":
                    login_admin()  # Login sebagai admin
                elif pilihan_role == "2":
                    login_customer()  # Login sebagai customer
                elif pilihan_role == "3":
                    print("Berhasil Kembali Ke Menu Utama")
                else:
                    print("Pilihan opsi tidak Valid, Mohon memilih opsi yang tersedia!")
            elif opsi == "3":
                print("Terimakasih Telah menggunakan jasa kami, sampai bertemu lagi")
                break
            else:
                print("Pilihan Opsi tidak valid, Mohon memilih opsi yang tersedia!")

        # Menangani KeyboardInterrupt ketika Ctrl+C ditekan
        except KeyboardInterrupt:
            print("\n======================================")
            print("\nDiciptakan Error Untuk Di Atasi\nBukan Dihindari Apalagi Ditinggal Pergi\n")
            print("=======================================")
            continue  # Melanjutkan ke iterasi berikutnya tanpa keluar dari program

        # Menangani kesalahan lain yang mungkin muncul
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

# Memanggil fungsi tampilan utama
tampilan_utama()