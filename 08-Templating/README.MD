# 08: HTML Generation with Templating — Analysis

## Analysis

- Menambahkan **pyramid_chameleon** sebagai renderer untuk menghasilkan HTML menggunakan template `.pt`.
- View kini hanya **mengirim data dictionary**, tanpa mencampur logika Python dengan markup HTML.
- Pendekatan ini membuat testing lebih mudah:  
  pengujian cukup memeriksa data yang dikembalikan view tanpa perlu memvalidasi HTML.
- Template dapat digunakan ulang oleh banyak view, mendukung DRY dan konsistensi tampilan.

## Extra Credit

- Pyramid memungkinkan penggunaan **renderer lain** (Jinja2, Mako, JSON, dll) tanpa mengubah pola view.  
  Cukup mengganti renderer dan template file.
- Memudahkan migrasi atau integrasi desain baru.

---