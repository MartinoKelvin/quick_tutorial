from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    # 🔹 Buat session factory untuk signed cookie
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')

    config = Configurator(
        settings=settings,
        session_factory=my_session_factory,  # 🔹 daftarkan ke Configurator
    )
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.scan('.views')
    return config.make_wsgi_app()
