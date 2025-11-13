# 13: Static Assets (CSS/JS/Images) — Analysis

## Analysis

- Pyramid menggunakan **add_static_view** untuk mempublikasikan folder berisi file statis seperti **CSS**, **JavaScript**, dan **gambar**.
- Menghasilkan URL yang aman dan fleksibel melalui **request.static_url()**, sehingga path final tidak perlu ditulis manual.
- Memungkinkan integrasi CSS/JS secara **proper** ke dalam template, mirip dengan framework web modern lainnya.
- Pada proses testing, dapat dipastikan bahwa file statis benar-benar **ter-deploy** dan dapat diakses oleh aplikasi.

## Extra Credit

- Pyramid juga menyediakan **static_path**, yaitu fungsi untuk mendapatkan *path lokal* ke file statis — bukan URL publik.
- Cocok untuk penggunaan internal server-side, misalnya saat membaca file langsung dari disk.

---


