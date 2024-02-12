import web

from mvc.models.m_index import ModeloIndex

render = web.template.render('mvc/views/')

m_index = ModeloIndex()
   
class Index:
    def GET(self):
        try:
            datos = [
                m_index.nombre,
                m_index.email
            ]
            return render.index(datos)
        except Exception as e:
            print (f"Error 101 - index {e.args}")
            return render.error()
