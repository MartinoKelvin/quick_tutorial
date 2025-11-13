import colander
import deform
import deform.widget

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .models import DBSession, Page


class WikiPage(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.RichTextWidget(),
    )


class WikiViews:
    def __init__(self, request):
        self.request = request

    @property
    def wiki_form(self):
        schema = WikiPage()
        return deform.Form(schema, buttons=('submit',))

    @property
    def reqts(self):
        return self.wiki_form.get_widget_resources()

    # 🔹 List semua page
    @view_config(route_name='wiki_view', renderer='wiki_view.pt')
    def wiki_view(self):
        pages = DBSession.query(Page).order_by(Page.title)
        return dict(title='Wiki View', pages=pages)

    # 🔹 Tambah page baru
    @view_config(route_name='wikipage_add',
                 renderer='wikipage_addedit.pt')
    def wikipage_add(self):
        form = self.wiki_form

        # GET → render form kosong
        if 'submit' not in self.request.params:
            return dict(form=form.render())

        # POST → proses dan validasi
        controls = self.request.POST.items()
        try:
            appstruct = form.validate(controls)
        except deform.ValidationFailure as e:
            # Form tidak valid
            return dict(form=e.render())

        # Valid → insert ke database
        new_title = appstruct['title']
        new_body = appstruct['body']
        DBSession.add(Page(title=new_title, body=new_body))

        # Ambil kembali Page yang baru dibuat, untuk dapatkan uid
        page = DBSession.query(Page).filter_by(title=new_title).one()
        new_uid = page.uid

        url = self.request.route_url('wikipage_view', uid=new_uid)
        return HTTPFound(url)

    # 🔹 Lihat satu page
    @view_config(route_name='wikipage_view', renderer='wikipage_view.pt')
    def wikipage_view(self):
        uid = int(self.request.matchdict['uid'])
        page = DBSession.query(Page).filter_by(uid=uid).one()
        return dict(page=page)

    # 🔹 Edit page
    @view_config(route_name='wikipage_edit',
                 renderer='wikipage_addedit.pt')
    def wikipage_edit(self):
        uid = int(self.request.matchdict['uid'])
        page = DBSession.query(Page).filter_by(uid=uid).one()

        wiki_form = self.wiki_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = wiki_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(page=page, form=e.render())

            # Update record
            page.title = appstruct['title']
            page.body = appstruct['body']

            url = self.request.route_url('wikipage_view', uid=uid)
            return HTTPFound(url)

        # GET → render form dengan data page
        form = wiki_form.render(dict(
            uid=page.uid,
            title=page.title,
            body=page.body,
        ))

        return dict(page=page, form=form)
