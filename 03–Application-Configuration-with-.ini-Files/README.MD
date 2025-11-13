# 03: Writing Views and Routes — Analysis

## Analysis

- Menjelaskan **pemisahan antara route dan view**, sehingga URL dan logika pemrosesan tidak bercampur.
- **Router** akan mencocokkan pola URL tertentu lalu memanggil **view function** yang sesuai.
- Pendekatan ini membuat view lebih mudah di-maintain, di-organize, dan membantu skala aplikasi menjadi lebih besar.
- Memperkenalkan dekorator **@view_config** untuk mendeklarasikan view secara eksplisit (termasuk route, renderer, dan pengaturan lainnya).

## Extra Credit

- Jika terdapat banyak route dengan pola mirip, **urutan pendaftaran route menjadi penting** karena dapat bertabrakan — Pyramid mengharuskan deklarasi eksplisit agar aman.
- View dapat di-**scan** secara otomatis menggunakan `config.scan()`, sehingga developer cukup mendeklarasikan view dengan `@view_config` tanpa perlu mendaftarkan secara manual.

