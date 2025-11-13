from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Aktifkan Jinja2 renderer
    config.include('pyramid_jinja2')

    # Routes
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')

    config.scan('.views')
    return config.make_wsgi_app()
