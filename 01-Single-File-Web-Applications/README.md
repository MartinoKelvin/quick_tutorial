# 🧩 01 - Single File Web Application (Pyramid)

## 🎯 Tujuan

Mempelajari cara membuat aplikasi web sederhana menggunakan **Pyramid Framework** dalam **satu file Python**.
Percobaan ini memperkenalkan konsep **WSGI**, **request-response**, dan **view function** sebagai pondasi dasar aplikasi web di Python.

---

## ⚙️ Persiapan Lingkungan

1. Pastikan Python sudah terinstal (disarankan Python 3.10+).
2. Buka PowerShell dan arahkan ke folder proyek:
   ```powershell
   cd "D:\Kuliah\Semester 5\tugas-tambahan\01-Single-File-Web-Applications"
   ```
3. Buat virtual environment dan aktifkan:
   ```powershell
   python -m venv .venv
    .\.venv\Scripts\Activate.ps1 

   ```
4. Jika PowerShell menolak eksekusi script, jalankan:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

   ```
5. Instal dependensi Pyramid dan Waitress:
   ```powershell
   pip install pyramid waitress


   ```

## 🚀 Menjalankan Aplikasi

1. Jalankan file app.py:
   ```powershell
   python app.py

   ```
2. Buka browser dan kunjungi alamat berikut:
   ```powershell
   http://localhost:6543/

   ```
3. Maka akan muncul halaman sederhana dengan teks:
   ```powershell
   <h1>Hello World!</h1>


   ```

## 📚 Analisis Percobaan

1. Tujuan Percobaan
   Menjalankan aplikasi web pertama menggunakan Pyramid untuk memahami alur request–response berbasis WSGI.
2. Analisis Baris
   * Baris print('Incoming request') menunjukkan setiap request yang masuk ke server.
   * Response('`<h1>`Hello World!`</h1>`') berfungsi untuk membentuk objek HTTP Response.
    * Configurator() memungkinkan pengembangan aplikasi dari skala kecil (single file) ke skala besar (modular).
3. Eksperimen Tambahan
    * Jika print('Incoming request') diganti menjadi print 'Incoming request', akan error karena Python 3 memerlukan tanda kurung.

    * Jika fungsi hello_world mengembalikan string biasa, akan muncul error karena Pyramid mengharapkan Response object.

    * Jika mengembalikan angka (return 123), muncul TypeError.

    * Jika menulis print xyz tanpa mendefinisikan xyz, muncul NameError di terminal saat halaman diakses ulang.
4. Konsep WSGI (Web Server Gateway Interface)
    * Merupakan standar komunikasi antara server web (misalnya Waitress) dan aplikasi Python.

    * Konsep ini merupakan evolusi dari CGI (Common Gateway Interface), tetapi lebih efisien karena aplikasi tetap berjalan tanpa restart di setiap request.