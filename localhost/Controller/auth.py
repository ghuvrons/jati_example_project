from Jati.Base.Controller import Controller

class auth(Controller):
    Services = {}
    Models = {}
    def index(self):
        return "Hello World"

    def generate_token(self, **kw):
        # user = self.Models["user"]()
        # users = user.search().limit(2)
        # for u in users:
        #     print([users])

        auth = kw['auth']
        token = auth.generateToken()
        return {
            "token": token
        }

    def _user(self, **kw):
        auth = kw['auth']
        return {
            "data": auth.user.email
        }