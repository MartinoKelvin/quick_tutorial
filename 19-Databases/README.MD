# 19: Databases Using SQLAlchemy — Analysis

## Analysis

- Pyramid menggunakan **SQLAlchemy ORM** untuk mendefinisikan model (contohnya model `Page`).
- **DBSession** dipakai untuk mengelola session database secara global agar mudah digunakan di seluruh aplikasi.
- Integrasi dengan Pyramid memakai **zope.sqlalchemy**, yang menyambungkan session ORM ke **transaction manager Pyramid**.
- Pyramid menyediakan **CLI tool** seperti `initialize_tutorial_db` untuk membuat dan menginisialisasi database.
- View CRUD cukup menyesuaikan query ke database menggunakan SQLAlchemy.

## Extra Credit

- Pyramid lebih memilih desain **eksplisit** dan tidak bergantung pada “magic framework” yang menyembunyikan detail penting.
- Transaction manager meminimalkan risiko **commit tidak sengaja** dan memastikan atomicity.

---