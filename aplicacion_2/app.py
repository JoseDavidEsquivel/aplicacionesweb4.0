# Framework web.py
import web

# Rutas de los controladores
urls = (
    '/(.*)', 'mvc.controllers.hello.Hello' # El ultimo elemento se llamara como la clase que hay en el controlador
    )
app = web.application(urls, globals())

# Punto de Entrada
if __name__ == "__main__":
    app.run()