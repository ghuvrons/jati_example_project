from Jati.Base.Model import Model

class User(Model):
    DB = "db1"
    TABLE = 'user'

    def _attributtes(self):
        return {
            "name": Model._string()
        }