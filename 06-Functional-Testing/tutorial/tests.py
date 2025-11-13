import unittest
from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        from tutorial import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h1>Hello World!</h1>", response.body)  # cek isi body (bytes)


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        # Bungkus WSGI app via entry factory main({})
        from tutorial import main
        app = main({})  # global_config kosong sudah cukup
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_hello_world(self):
        # Simulasikan GET ke "/" dan cek 200 + isi HTML
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Hello World!</h1>', res.body)

        # (Opsional) contoh lain:
        # self.assertTrue(res.content_type.startswith("text/html"))
        # self.assertIn("Hello World!", res.text)  # res.text -> str (decoded)
