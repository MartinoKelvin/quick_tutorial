from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        # Redirect dari "/" ke "/plain"
        return HTTPFound(location='/plain')

    @view_config(route_name='plain')
    def plain(self):
        # Ambil query param: /plain?name=Jane
        name = self.request.params.get('name', 'No Name Provided')

        body = 'URL %s with name: %s' % (self.request.url, name)
        return Response(
            content_type='text/plain',
            body=body
        )
