# 09: Organizing Views with View Classes — Analysis

## Analysis

- Pyramid memungkinkan pengelompokan banyak view dalam **satu class**, sehingga struktur kode menjadi lebih rapi dan terorganisir.
- Menggunakan **@view_defaults** untuk mengurangi repetisi konfigurasi seperti renderer atau route prefix.
- Semua method di dalam class berbagi **state yang sama**, terutama akses ke `self.request`.
- Pada proses testing, view class perlu diinisialisasi sebagai instance sebelum sebuah method diuji.

## Extra Credit

- View class memudahkan pengembangan **REST-style endpoints**, seperti method `get()`, `post()`, `put()`, `delete()` dalam satu class.
- Mendukung organization code yang lebih scalable dan maintainable untuk aplikasi besar.

---