from Jati.Base.Controller import Controller

class site(Controller):
    Services = {}
    def index(self):
        return "Hello World"

    def error(self, **kw):
        kw['respond'].set_header('Content-Type', "application/json")
        return {
            "status": kw['error_code'],
            "message": kw['error_message']
        }