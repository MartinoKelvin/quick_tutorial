from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Definisi route (nama route bebas, URL path bebas)
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')

    # Scan modul views.py untuk mencari @view_config
    config.scan('.views')

    return config.make_wsgi_app()
