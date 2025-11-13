# 05: Creating a Test Suite — Analysis

## Analysis

- Memperkenalkan dua jenis pengujian penting dalam aplikasi Pyramid:
  - **Unit Test** → Menguji fungsi view secara langsung tanpa server.
  - **Functional Test** → Menggunakan *WebTest* untuk mensimulasikan HTTP request nyata ke aplikasi.
- Memberikan dasar praktik **Test-Driven Development (TDD)** agar developer dapat membangun fitur secara terstruktur dan aman.
- Test suite membantu memastikan view, route, dan respons aplikasi bekerja sesuai ekspektasi di seluruh tahap pengembangan.

## Extra Credit

- **DummyRequest** dari Pyramid memungkinkan pengujian view tanpa perlu menjalankan server WSGI, sehingga proses pengujian jauh lebih cepat dan efisien.

---