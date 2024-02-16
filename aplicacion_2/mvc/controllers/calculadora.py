import web

render = web.template.render('mvc/views')

class Calculadora:
    def GET(cls, resultado=""):
        return render.calculadora(resultado)

    def POST(self):
        form = web.input()
        num1 = float(form.num1)
        num2 = float(form.num2)
        resultado = num1 * num2
        return render.calculadora(resultado,num2,num1)

