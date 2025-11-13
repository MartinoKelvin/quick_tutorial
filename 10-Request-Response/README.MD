# 10: Handling Web Requests and Responses — Analysis

## Analysis

- Pyramid menyediakan fleksibilitas penuh untuk **memanipulasi request dan response** dalam aplikasi web.
- Redirect dapat dilakukan menggunakan **HTTPFound**, baik dengan `return` maupun `raise`.
- Data dari query string atau form dapat diakses melalui **request.params**.
- Response dapat dikustomisasi, misalnya mengubah **header**, **status code**, atau **content type**.

## Extra Credit

- `raise HTTPFound()` menghasilkan perilaku sama dengan `return HTTPFound()`,  
  namun menggunakan mekanisme **exception-based flow** sehingga cocok untuk menghentikan alur view lebih awal.

---