from Jati.Base.Controller import Controller

class site(Controller):
    Services = {}
    def index(self, req):
        return "Hello World"

    def error(self, req, code, message):
        req.set_respone_header('Content-Type', "application/json")
        return {
            "status": code,
            "message": message
        }