# 15: More with View Classes — Analysis

## Analysis

- View class sangat cocok untuk membangun **REST-like flows** seperti GET, POST, dan DELETE dalam satu struktur terorganisir.
- Satu URL dapat memiliki banyak perilaku berbeda berdasarkan **HTTP method**.
- **@view_defaults** digunakan untuk menyederhanakan konfigurasi global, seperti renderer atau route.
- View class memungkinkan berbagi **state**, helper function, atau property di seluruh method melalui `self`.
- Pola ini menghasilkan arsitektur yang bersih, rapi, dan mudah dimaintain ketika endpoint semakin kompleks.

## Extra Credit

- Menggunakan **@property** membuat nilai diakses otomatis tanpa tanda kurung, ideal untuk helper atau computed values.
- Predicate **request_param** dapat digunakan untuk menghindari “POST conflict”, yaitu kondisi ketika dua view POST berpotensi tumpang tindih.

---