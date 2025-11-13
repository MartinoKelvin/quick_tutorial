# 14: AJAX Development with JSON Renderer — Analysis

## Analysis

- Pyramid menyediakan **JSON renderer** yang otomatis mengubah dictionary Python menjadi **JSON response**.
- Pola view tetap sama—view hanya mengembalikan dictionary, namun renderer menentukan outputnya.
- Pyramid memungkinkan “menumpuk” banyak `@view_config` pada satu fungsi untuk menyediakan **endpoint HTML dan JSON sekaligus**.
- Fitur ini sangat cocok untuk membuat **API ringan**, AJAX endpoint, atau front-end apps berbasis JavaScript.

## Extra Credit

- JSON renderer dapat dipicu menggunakan **accept predicate**, misalnya dengan header:
