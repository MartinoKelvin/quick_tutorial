import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        # Siapkan konfigurasi Pyramid untuk test (opsional pada kasus sederhana)
        self.config = testing.setUp()

    def tearDown(self):
        # Bereskan konfigurasi setelah test
        testing.tearDown()

    def test_hello_world(self):
        # Import view DI DALAM test agar terisolasi (menghindari efek samping import global)
        from tutorial import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)

        # Cek status code
        self.assertEqual(response.status_code, 200)

        # (Opsional) Cek isi body HTML
        # Response.body adalah bytes; decode ke utf-8.
        self.assertIn(b"<h1>Hello World!</h1>", response.body)
