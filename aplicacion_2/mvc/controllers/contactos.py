import web
from mvc.models.m_contactos import ModeloContactos

render = web.template.render('mvc/views/', base='layout')

class Contactos:
    def GET(self):
        modelo_contactos = ModeloContactos()
        contactos = modelo_contactos.contactos
        return render.contactos(contactos)
