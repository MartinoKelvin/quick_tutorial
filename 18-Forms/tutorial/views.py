import colander
import deform
import deform.widget

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

# 🔹 Dummy data: "database" kecil di memory
pages = {
    '100': dict(uid='100', title='Page 100', body='<em>100</em>'),
    '101': dict(uid='101', title='Page 101', body='<em>101</em>'),
    '102': dict(uid='102', title='Page 102', body='<em>102</em>'),
}


# 🔹 Colander schema untuk satu wiki page
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
        # tombol submit bernama "submit"
        return deform.Form(schema, buttons=('submit',))

    @property
    def reqts(self):
        # resource JS/CSS yang dibutuhkan widget Deform
        return self.wiki_form.get_widget_resources()

    # 🔹 Halaman utama: list semua page
    @view_config(route_name='wiki_view', renderer='wiki_view.pt')
    def wiki_view(self):
        return dict(pages=pages.values())

    # 🔹 Tambah page (GET form + POST submit)
    @view_config(route_name='wikipage_add',
                 renderer='wikipage_addedit.pt')
    def wikipage_add(self):
        form = self.wiki_form

        # Pertama kali, GET → render form kosong
        if 'submit' not in self.request.params:
            return dict(form=form.render())

        # Kalau ada "submit" → proses POST
        controls = self.request.POST.items()
        try:
            appstruct = form.validate(controls)
        except deform.ValidationFailure as e:
            # Form TIDAK valid → render lagi dengan error
            return dict(form=e.render())

        # Form valid → buat UID baru dan simpan data
        last_uid = int(sorted(pages.keys())[-1])
        new_uid = str(last_uid + 1)
        pages[new_uid] = dict(
            uid=new_uid,
            title=appstruct['title'],
            body=appstruct['body'],
        )

        # Redirect ke halaman view page tersebut
        url = self.request.route_url('wikipage_view', uid=new_uid)
        return HTTPFound(url)

    # 🔹 Lihat satu page
    @view_config(route_name='wikipage_view', renderer='wikipage_view.pt')
    def wikipage_view(self):
        uid = self.request.matchdict['uid']
        page = pages[uid]
        return dict(page=page)

    # 🔹 Edit page (GET form pre-filled + POST update)
    @view_config(route_name='wikipage_edit',
                 renderer='wikipage_addedit.pt')
    def wikipage_edit(self):
        uid = self.request.matchdict['uid']
        page = pages[uid]
        form = self.wiki_form

        # Kalau POST submit
        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = form.validate(controls)
            except deform.ValidationFailure as e:
                # Form tidak valid → render lagi dengan data + error
                return dict(page=page, form=e.render())

            # Valid → update data dan redirect ke view
            page['title'] = appstruct['title']
            page['body'] = appstruct['body']

            url = self.request.route_url('wikipage_view', uid=page['uid'])
            return HTTPFound(url)

        # Kalau GET → render form dengan data awal (page)
        rendered_form = form.render(page)
        return dict(page=page, form=rendered_form)
