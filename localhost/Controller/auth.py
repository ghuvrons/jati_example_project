from Jati.Base.Controller import Controller

class auth(Controller):
    Services = {}
    Models = {}
    def index(self, req):
        return "Hello World"

    def generate_token(self, req):
        user = self.Models["user"]()
        users = user.search()
        print([users])
        # token = self.Services["auth"].generate_token()
        # return {
        #     "token": token,
        #     "data": req.data
        # }
