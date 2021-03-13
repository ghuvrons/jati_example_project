import jwt
from Jati.Base.Service import Service

class Auth(Service):
    def __init__(self):
        Service.__init__(self)
        self.timeout = None
        
    def generate_token(self):
        print(self.Databases['db1'])
        encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
        return encoded_jwt