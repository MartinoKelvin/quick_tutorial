# 16: Application Logging — Analysis

## Analysis

- Pyramid menggunakan **modul logging standar Python**, sehingga integrasinya stabil dan familiar.
- Konfigurasi logging diletakkan di file **.ini** (misalnya `development.ini`), bukan di-hardcode di source code.
- Logging mempermudah proses **debugging**, karena view maupun komponen lain dapat menulis log dengan mudah.
- Integrasi dengan **pyramid_debugtoolbar** memungkinkan inspeksi visual log, request, dan exception secara interaktif.

## Extra Credit

- Level log dapat diatur per-namespace, misalnya:
  - SQLAlchemy
  - Pyramid internal
  - Namespace aplikasi sendiri (`tutorial.views`, dll)
- Memberikan kendali penuh untuk memfilter noise log dan fokus pada area tertentu.

---