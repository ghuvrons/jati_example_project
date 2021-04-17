from Jati.Base.Auth import AuthModel
from Jati.Database.SQL.Model import Model
from .Auth import UserRolePermission

class User(Model, AuthModel):
    DB = "db1"
    TABLE = 'user'

    def __init__(self, **kw):
        Model.__init__(self, **kw)
        self.roles = []
        self.permissions = []

        for rp in self.rolesAndPermission:
            if rp.role:
                self.roles.append(rp.role)
            elif rp.permission:
                self.permissions.append(rp.permission)

    def _attributtes(self):
        return {
            "id": Model._integer(),
            "name": Model._string(),
            "rolesAndPermission" : Model._hasMany(UserRolePermission, on={
                "id_user" : "id"
            })
        }
    
    @staticmethod
    def authenticate(username, password):
        user = User.one(email=username, password=password)
        return user

    def __is__(self, param):
        if param == "manager": return True
        return False
