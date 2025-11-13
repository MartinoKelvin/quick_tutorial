# 12: Templating with Jinja2 — Analysis

## Analysis

- Pyramid mendukung berbagai **sistem templating** seperti **Jinja2**, **Mako**, dan **Chameleon**, memberi developer fleksibilitas memilih teknologi tampilan.
- Aktivasi Jinja2 sangat mudah, cukup memanggil:
  ```python
  config.include('pyramid_jinja2')

- **View tetap sama**, hanya file templatenya berubah menjadi .jinja2.
- Menunjukkan bahwa arsitektur Pyramid tidak mengunci developer pada satu renderer tertentu —   sangat fleksibel dan modular.

## Extra Credit

- Renderer seperti Jinja2 bisa di-include otomatis melalui package includes pada Pyramid.
- Developer dapat menambah renderer lain tanpa mengubah pola penulisan view.