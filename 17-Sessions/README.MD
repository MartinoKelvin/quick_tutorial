# 17: Transient Data Using Sessions — Analysis

## Analysis

- Session digunakan untuk menyimpan **data sementara** seperti counter kunjungan, shopping cart, atau flash message.
- Pyramid biasanya memakai **SignedCookieSessionFactory**, yang menyimpan data terenkripsi di dalam cookie.
- Session memiliki perilaku seperti **dictionary**, sehingga mudah dibaca/tulis menggunakan key–value.
- Dapat menggunakan property pada view class untuk menghitung counter otomatis setiap kali request datang.

## Extra Credit

- **Flash messages** memungkinkan data disimpan hanya selama **1 request–response cycle** — cocok untuk notifikasi setelah redirect.
- Session mendukung banyak backend jika butuh storage lebih besar (Redis, database, dsb).

---