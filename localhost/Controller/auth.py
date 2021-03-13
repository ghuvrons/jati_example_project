from Jati.Base.Controller import Controller

class auth(Controller):
    Services = {}
    def index(self, req):
        return "Hello World"

    def generate_token(self, req):
        token = self.Services["auth"].generate_token()
        return {
            "token": token,
            "data": req.data
        }
