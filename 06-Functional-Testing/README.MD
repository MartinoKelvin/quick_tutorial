# 06: Returning Template-Based HTML — Analysis

## Analysis

- Memperkenalkan **renderers** dalam Pyramid yang memungkinkan view mengembalikan HTML melalui file template.
- View cukup mengembalikan **dictionary data**, sementara HTML berada sepenuhnya di file template (misalnya Chameleon `.pt`).
- Pendekatan ini menciptakan desain yang lebih bersih dengan **pemisahan antara logika Python dan tampilan HTML**.
- Cocok untuk aplikasi web yang membutuhkan struktur halaman rapi, reusable, dan mudah di-maintain.

## Extra Credit

- Pyramid menyediakan `render_to_response()` apabila developer perlu memanipulasi objek `Response` secara manual sebelum dikirim ke browser.
- Fleksibel untuk output lain seperti XML, JSON, atau plain text.

---