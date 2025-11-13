# 18: Forms & Validation with Deform — Analysis

## Analysis

- Pyramid memperkenalkan dua komponen powerful:
  - **Colander** → untuk membuat *schema* dan *validation rules*.
  - **Deform** → untuk *UI form generation* + *automatic validation*.
- Deform dapat **menghasilkan layout form otomatis** dari schema, termasuk widget, label, dan pesan error.
- Pola standar adalah **self-posting form**, yaitu:
  - GET → menampilkan form kosong
  - POST → memproses input dan menampilkan hasil atau pesan error
- Jika validasi gagal, Deform menghasilkan **ValidationFailure** yang otomatis menampilkan form beserta error.

## Extra Credit

- Sistem widget Deform dapat **memuat resource (CSS/JS)** secara otomatis melalui `form.get_widget_resources()`.
- Sangat cocok untuk UI yang dinamis tanpa banyak boilerplate HTML.

---