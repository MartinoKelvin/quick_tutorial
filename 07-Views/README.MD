# 07: Organizing Code Layout — Analysis

## Analysis

- Proyek Pyramid diorganisasi menjadi beberapa **modul terpisah** seperti:
  - `views/` untuk kumpulan view
  - `routes/` untuk manajemen route
  - `templates/` untuk file HTML/Chameleon
  - `tests/` untuk unit test dan functional test
- Pemisahan ini membuat proyek lebih **mudah dirawat**, terutama saat aplikasi mulai membesar.
- Mengikuti **konvensi struktur proyek** Pyramid sehingga developer lain lebih mudah memahami dan berkolaborasi.

## Extra Credit

- Struktur yang modular mencegah terjadinya **god-file**, yaitu file besar yang menampung terlalu banyak kode sehingga sulit di-maintain.
- Setiap modul dapat dikembangkan, diuji, dan di-refactor secara independen.

---