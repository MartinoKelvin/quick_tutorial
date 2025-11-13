# 11: Dispatching URLs to Views with Routing — Analysis

## Analysis

- Pyramid menggunakan **routing berbasis pola** seperti `/{first}/{last}` untuk menangkap bagian dinamis dari URL.
- Nilai parameter hasil pencocokan pola disimpan di **request.matchdict**, yang menjadi sumber data utama bagi view.
- Routing Pyramid bersifat **sangat eksplisit**, sehingga developer mengetahui secara pasti bagaimana setiap URL dipetakan.
- Pendekatan ini memudahkan pembuatan URL yang **bersih**, terstruktur, dan cocok untuk desain **REST-friendly endpoints**.

## Extra Credit

- Jika URL tidak cocok dengan pola yang didefinisikan, Pyramid langsung mengembalikan **404 Not Found** —  
  Pyramid **tidak membuat asumsi** atau menebak rute.

---