## SISTEM MANAJEMEN PENGIRIMAN BARANG <br><br>

--------------------------------------------
|          NAMA               |    NIM     | 
|-----------------------------|------------|            
| Christian Amsal Asimaro L.T | 2409116057 | 
| Muhammad Irdhan Nur Faudzan | 2409116077 | 
| Ghendida Gantari Ayari      | 2409116080 |
--------------------------------------------
<br>

## Gambar Flowchart

![Flowchart_PA](https://github.com/user-attachments/assets/1b0f965b-5701-4925-bf31-b0035a62dc43)

<br>

![flowchart_PA2](https://github.com/user-attachments/assets/498c669e-3ce6-4418-b127-8fbc50019877)

<br>

![flowchart_PA3](https://github.com/user-attachments/assets/2a14e95c-13f6-477a-bc3f-6bd8ea561c51)

<br>

![flowchart_PA4](https://github.com/user-attachments/assets/f5e54d19-5904-4e2d-ba40-551e449b5d69)

<br><br>

## Output Dari Program

### Menu Customer
![WhatsApp Image 2024-11-09 at 13 17 16_247c7803](https://github.com/user-attachments/assets/c1734710-785f-485b-8ec5-1fe1c55359bd)
Di menu awal ada 3 pilihan yaitu:
- Registrasi Akun
- Login
- Exit
<br>

![WhatsApp Image 2024-11-09 at 13 18 35_fd04adc4](https://github.com/user-attachments/assets/7bc561ef-e56c-4a5a-86cf-af4744ad8290)
Jika belum memeliki akun, sebagai customer maka bisa membuat akun terlebih dahulu dan jika sudah berhasil
login kembali dengan akun yang sudah dibuat.
<br>

![WhatsApp Image 2024-11-09 at 13 19 33_c35e73ef](https://github.com/user-attachments/assets/1ca678d6-b7a7-4bda-b85e-492b76b9ee31)
Jika baru membuat akun maka harus top up terlebih dahulu agar bisa membuat pengiriman.
<br>

![WhatsApp Image 2024-11-09 at 13 21 30_7b6e88c1](https://github.com/user-attachments/assets/9486d296-2cfe-4155-8099-8cd64a7be2d7)
Setelah selesai top up maka bisa lanjut ke menu Buat Pengiriman, di menu ini saldo akan otomatis terpotong
sesuai dengan berat barang yang dikirim.
<br>

![WhatsApp Image 2024-11-09 at 13 22 16_b94aaf23](https://github.com/user-attachments/assets/0aada821-0beb-4ef3-85d3-877800b5e539)
Customer bisa melihat pengiriman dia di menu lihat pengiriman, di menu ini hanya bisa melihat pengiriman
kita sendiri jadi tidak bisa melihat pengiriman orang lain.
<br>

![WhatsApp Image 2024-11-09 at 13 22 58_b575869f](https://github.com/user-attachments/assets/a3be9225-7a33-4284-95aa-d3c79f01258f)
Jika sudah selesai maka bisa logout dan kembali ke menu utama.
<br>

### Menu Admin

![WhatsApp Image 2024-11-09 at 13 23 48_be5410a2](https://github.com/user-attachments/assets/e4abe805-a3ad-4a17-a21c-5729a08e1f5b)
Untuk masuk ke menu admin harus login dan username: admin, password: admin123.
dan terdapat 6 pilihan untuk admin:
- Ubah/Update Status Data Pengiriman
- Hapus Data Pengiriman
- Lihat Data Pengiriman
- Cari Data Pengiriman
- Sorting Data Pengiriman
- Logout
<br>

![WhatsApp Image 2024-11-09 at 13 24 48_bc81ad87](https://github.com/user-attachments/assets/7a4194c7-01c6-4802-9115-75f4e15aa198)
Di menu ke 1 yaitu admin bisa mengubah/mengupdate status pengiriman.
<br>

![WhatsApp Image 2024-11-09 at 13 25 47_d3e64139](https://github.com/user-attachments/assets/9f3fa6e7-35b7-4689-aaff-3aeb14a09df8)
Di menu 2 yaitu admin bisa menghapus pengiriman.
<br>

![WhatsApp Image 2024-11-09 at 13 35 44_e7c8153e](https://github.com/user-attachments/assets/7d166c0e-88a7-49a3-afd0-44c7c89ddf08)
Di menu 3 yaitu admin bisa melihat semua pengiriman yang dibuat oleh para customer.
<br>

![WhatsApp Image 2024-11-09 at 13 36 39_da725b5f](https://github.com/user-attachments/assets/b7ece5e5-5886-496f-8846-7dc2697ebbe5)
Di menu 4 yaitu admin bisa mencari data pengiriman dengan mengetik nama barangnya.
<br>

![WhatsApp Image 2024-11-09 at 13 37 43_86c7a206](https://github.com/user-attachments/assets/e4f7a8cf-3dea-40f0-b5e9-84955b5ee2cd)
![WhatsApp Image 2024-11-09 at 13 38 08_1b92928e](https://github.com/user-attachments/assets/9512fd7e-05f1-4c1e-82df-2ee8102edfa9)
Di menu 5 yaitu admin bisa melakukan shorting berdasarkan nama barang, kota tujuan, tanggal pengiriman.
<br>

![WhatsApp Image 2024-11-09 at 13 38 50_e60ab0e4](https://github.com/user-attachments/assets/be3d2aaa-e3ff-41fa-93f0-7e1c367ac884)
Di menu 6 ini untuk keluar dan kembali ke menu utama
<br><br>

## Susunan Code

![code](https://github.com/user-attachments/assets/89697b8e-0b66-4097-9928-0f10a0e2c2ea)
- Mengimpor PrettyTable untuk membuat dan menampilkan data dalam bentuk tabel yang lebih rapi dan terstruktur, seperti pada menu login atau daftar pengiriman.
- Mengimpor csv yang digunakan untuk membaca dan menulis data dalam format CSV. ini berguna untuk menyimpan dan memuat data pengguna (Akun_Pengguna.csv) dan pengiriman (All_Data_Pengiriman.csv).
- Mengimpor pwinput untuk mengamankan input password dari pengguna. Ini memungkinkan pengguna untuk mengetikkan password tanpa terlihat di layar.
- Mendefinisikan variabel konstan yang menyatakan status pengiriman yang belum dibayar. Digunakan untuk menunjukkan status pengiriman ketika pengiriman baru dibuat dan belum diproses lebih lanjut.
- Mendefinisikan variabel konstan yang menunjukkan status pengiriman yang sedang menunggu antrian untuk diproses. Ini digunakan setelah pengiriman berhasil dibuat dan menunggu untuk diproses lebih lanjut.
- Mendefinisikan nama file CSV yang digunakan untuk menyimpan data akun pengguna, termasuk username, password, dan saldo mereka. Program membaca dan menulis data di file ini untuk melakukan otentikasi dan memanipulasi saldo pengguna.
- Mendefinisikan nama file CSV yang menyimpan data pengiriman. File ini digunakan untuk menyimpan dan membaca semua informasi tentang pengiriman yang dibuat, termasuk nama pengirim, penerima, status pengiriman, dll.
<br>

![fungsi tampilan_login](https://github.com/user-attachments/assets/4385997d-65f6-4a4d-b7ba-12f3f5c2af63)
- Fungsi ini menggunakan PrettyTable untuk menampilkan menu login dengan opsi "ADMIN," "CUSTOMER," dan "KEMBALI."
<br>

![fungsi registrasi_akun](https://github.com/user-attachments/assets/d564e7bd-9c92-45a5-b4e7-adfb09062ee4)
- Fungsi ini mengharuskan pengguna untuk membuat username dan password, lalu menyimpannya dalam file Akun_Pengguna.csv. Saldo awal pengguna diatur ke 0.
<br>

![fungsi validasi_akun](https://github.com/user-attachments/assets/0d52936e-f628-41e4-a296-7611c9a39785)
- Fungsi ini memvalidasi akun pengguna (customer) dengan mencocokkan username dan password yang dimasukkan dengan data yang ada di Akun_Pengguna.csv. Mengembalikan True jika cocok, False jika tidak.
<br>

![fungsi validasi_akun_admin](https://github.com/user-attachments/assets/b9c5a703-5410-4924-8c7d-14ba01b9036c)
- Fungsi ini memvalidasi akun admin dengan username dan password statis ("admin" dan "admin123"). Mengembalikan True jika cocok, False jika tidak.
<br>

![fungsi tampilan_admin](https://github.com/user-attachments/assets/466af1af-86c0-4a97-9a06-10a0a0c9571e)
- Fungsi ini menggunakan PrettyTable untuk menampilkan opsi menu admin, seperti mengubah status pengiriman, menghapus pengiriman, melihat data pengiriman, mencari data, menyortir data, dan keluar (LogOut).
<br>

![fungsi login_admin](https://github.com/user-attachments/assets/8f1b6f90-9b9b-45f7-834e-b630913cdb48)
- Fungsi ini mengautentikasi admin dan memberikan akses ke menu admin. Setiap opsi pada menu memanggil fungsi yang relevan untuk melaksanakan operasi tertentu.
<br>

![fungsi tampilan_customer](https://github.com/user-attachments/assets/1efec789-5b6e-4061-915e-37aaca4598b7)
- Fungsi ini menggunakan PrettyTable untuk menampilkan opsi menu customer, seperti membuat pengiriman, melihat pengiriman, top-up saldo, dan keluar (LogOut).
<br>

![fungsi login_customer](https://github.com/user-attachments/assets/2a729b84-f99d-400e-8a7a-2901a4e02e74)
- Fungsi ini mengautentikasi customer dengan username dan password. Jika berhasil, menu customer akan muncul, memberikan opsi untuk membuat pengiriman, melihat pengiriman, melakukan top-up saldo, atau logout.
<br>

![fungsi buat_pengiriman](https://github.com/user-attachments/assets/21b03d54-d922-4b8c-a0c0-f974f00d47e7)
- Fungsi ini membuat data pengiriman baru. Pengguna memasukkan detail seperti nama barang, kota tujuan, nama pengirim, nama penerima, tanggal pengiriman, dan status pengiriman yang disetel ke "Menunggu Pembayaran."
Setelah memasukkan data, pengguna diberi pilihan untuk membayar. Jika memilih "y" (ya), akan memanggil fungsi pembayaran_Pengiriman(username). Jika tidak, pengiriman tertunda.
<br>

![fungsi tampilan_table](https://github.com/user-attachments/assets/8df3fa75-caff-4a6b-9bc5-65b28d50bbfa)
- Fungsi ini menampilkan tabel berdasarkan data yang diterima sebagai parameter. Berguna untuk menampilkan data pengiriman dengan rapi.
<br>

![fungsi lihat_pengiriman](https://github.com/user-attachments/assets/76b9eede-654b-48c0-bec6-1ccd7c6c1a61)
- Fungsi ini membaca semua data pengiriman dari All_Data_Pengiriman.csv dan menampilkannya dalam bentuk tabel jika ada data yang lengkap.
<br>

![fungsi top_up](https://github.com/user-attachments/assets/ffd733c9-d3cb-4321-8f87-afd0fa0180c3)
- Fungsi ini memungkinkan pengguna customer saldo mereka. Setelah saldo ditambah, data diperbarui di Akun_Pengguna.csv.
<br>

![fungsi lihat_pengiriman_customer](https://github.com/user-attachments/assets/7ec44fea-949e-4492-8d32-25e903f9b8e7)
- Fungsi ini hanya menampilkan data pengiriman untuk customer tertentu. Jika data pengiriman ditemukan berdasarkan nama pengirim, tabel akan ditampilkan; jika tidak, pesan "Anda Belum Memiliki Riwayat Pengiriman" akan muncul.
<br>

![fungsi ubah_data](https://github.com/user-attachments/assets/bba4d4ae-2362-412c-8824-1628f22ab79e)
- Fungsi ini memungkinkan admin mengubah status pengiriman tertentu berdasarkan ID pengiriman. Setelah diubah, data pengiriman yang diperbarui ditampilkan.
<br>

![fungsi hapus_pengiriman](https://github.com/user-attachments/assets/e020abc3-aa55-41f9-93d1-32a3722291b5)
- Fungsi ini untuk Menghapus data pengiriman berdasarkan ID pengiriman.
<br>

![fungsi fitur_cari](https://github.com/user-attachments/assets/f5715536-e9d6-4bf8-ad1f-76e1f8d8ca54)
- fungsi ini untuk Mencari pengiriman berdasarkan ID atau nama pengirim.
<br>

![fungsi fitur_sorting](https://github.com/user-attachments/assets/bb990d1c-87e2-4155-a481-99f0001dd0b8)
- fungsi ini untuk Menyortir data pengiriman berdasarkan kriteria yang sudah ada.
<br>

![fungsi pembayaran_pengiriman](https://github.com/user-attachments/assets/20af85dc-1d79-41ef-aacc-0c830295f5bd)
- fungsi ini untuk Memproses pembayaran pengiriman dan memperbarui status pengiriman.
<br>

![fungsi tampilan_utama](https://github.com/user-attachments/assets/a3acabc4-e224-4df1-8aa9-434765445c78)
- Menampilkan menu utama yang memungkinkan pengguna untuk memilih antara login sebagai admin, login sebagai customer, atau keluar dari program. Fungsi ini akan menampilkan opsi-opsi tersebut dan mengarahkan pengguna sesuai pilihan yang dipilih. 
<br>
<br>

## Disusun Oleh Kelompok 13, Sistem Informasi B2024.
