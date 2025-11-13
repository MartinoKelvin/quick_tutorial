# 04: Using URL Dispatch — Analysis

## Analysis

- Menjelaskan bagaimana Pyramid memproses **bagian dinamis** dari sebuah URL menggunakan pola route.
- Parameter yang ditangkap dari URL (misal: `/hello/john`) akan dimasukkan ke dalam `request.matchdict`.
- Pendekatan ini memisahkan **data dari URL** dengan **logika pemrosesan** di view, sehingga kode lebih bersih dan terstruktur.
- Memberikan fleksibilitas tinggi untuk membuat **REST-style endpoints** seperti `/users/1`, `/posts/99/edit`, dsb.

## Extra Credit

- Jika URL tidak sesuai dengan pola route (misalnya parameter hilang atau format salah), Pyramid akan memberikan **404 Not Found** karena URL tidak cocok dengan pola yang didefinisikan.
