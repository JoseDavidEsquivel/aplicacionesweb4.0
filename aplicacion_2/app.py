# Framework web.py
import web

# Rutas de los controladores
urls = (
    '/index', 'mvc.controllers.index.Index',
    '/productos', 'mvc.controllers.productos.Productos',
    '/contactos', 'mvc.controllers.contactos.Contactos'
    )
app = web.application(urls, globals())

# Punto de Entrada
if __name__ == "__main__":
    web.config.debug = False
    app.run()