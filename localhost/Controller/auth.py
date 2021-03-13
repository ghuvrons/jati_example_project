from Jati.Base.Controller import Controller
import jwt

class auth(Controller):
    def index(self, req):
        return "Hello World"

    def generate_token(self, req):
        encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
        return {
            "token": encoded_jwt,
            "data": req.data
        }
