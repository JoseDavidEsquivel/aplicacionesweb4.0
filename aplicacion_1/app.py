import web

urls = ("/", "hello",
        "/pagina2","pagina2"
        )
app = web.application(urls, globals())

class hello:
    def GET(self):
        return "Hello , pagina1"

class pagina2:
    def GET(self):
        return "Hello , pagina2"
    
class pagina3:
    def GET(self):
        return "Hello , pagina3489"

if __name__ == "__main__":
    app.run()