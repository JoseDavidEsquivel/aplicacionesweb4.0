# Framework web.py
import web

# Rutas de los controladores
urls = (
    '/', 'mvc.controllers.index.Index', # El ultimo elemento se llamara como la clase que hay en el controlador
    '/pagina2','mvc.controllers.pagina2.Pagina2'
    )
app = web.application(urls, globals())

# Punto de Entrada
if __name__ == "__main__":
    app.run()