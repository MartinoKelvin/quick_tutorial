from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Aktifkan pyramid_chameleon sebagai renderer
    config.include('pyramid_chameleon')

    # Definisikan routes
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')

    # Scan modul views.py
    config.scan('.views')

    return config.make_wsgi_app()
