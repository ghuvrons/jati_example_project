from Jati.Database.noSQL.Model import Model

class User2(Model):
    CACHE = {}
    DB = "db1"
    COLLECTION = 'auth_item'
    WHERE = {
        "type" : "role"
    }

    def __init__(self, *arg, **kw):
        Model.__init__(self, *arg, **kw)
        self.parents_id = []
        
    def _attributtes(self):
        return {
            "id": Model._integer(),
            "name": Model._string()
        }
