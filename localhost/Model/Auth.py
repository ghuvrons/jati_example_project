from Jati.Base.Model import Model

class Role(Model):
    CACHE = {}
    DB = "db1"
    TABLE = 'auth_item'
    WHERE = {
        "type" : "role"
    }

    def __init__(self, *arg, **kw):
        Model.__init__(self, *arg, **kw)
        self.parents_id = []
    
    def get_parents_id(self):
        if self.parent is not None:
            return self.parent.parents_id
        return []
    
    def set_parents_id(self):
        self.parents_id = [self.__id] + self.get_parents_id()
        
    def _attributtes(self):
        return {
            "id": Model._integer(),
            "name": Model._string(),
            "parent": Model._hasOne(Role, on={
                "id_parent" : "id"
            }),
            "permission": Model._hasMany(RolePermission, on={
                "id_role": "id"
            })
        }

    @classmethod
    def createFromDict(this_class, args, is_new = True):
        if this_class.PRIMARY_KEY in args and args[this_class.PRIMARY_KEY] in this_class.CACHE:
            return this_class.CACHE[args[this_class.PRIMARY_KEY]]

        model = this_class(**args)
        if not is_new:
            model.__updated__attr = {}
            if this_class.PRIMARY_KEY in args:
                model.__id = args[this_class.PRIMARY_KEY]
            model.set_parents_id()
            this_class.CACHE[model.__id] = model
        return model

class Permission(Model):
    CACHE = {}
    DB = "db1"
    TABLE = 'auth_item'
    WHERE = {
        "type" : "permission"
    }

    def __init__(self, *arg, **kw):
        Model.__init__(self, *arg, **kw)
        self.parents_id = []
    
    def get_parents_id(self):
        if self.parent is not None:
            return self.parent.parents_id
        return []
    
    def set_parents_id(self):
        self.parents_id = [self.__id] + self.get_parents_id()
        for r in self.roles:
            self.parents_id += r.role.parents_id

    def _attributtes(self):
        return {
            "id": Model._integer(),
            "name": Model._string(),
            "parent": Model._hasOne(Permission, on={
                "id_parent" : "id"
            }),
            "roles": Model._hasMany(RolePermission, on={
                "id_permission": "id"
            })
        }

    @classmethod
    def createFromDict(this_class, args, is_new = True):
        if this_class.PRIMARY_KEY in args and args[this_class.PRIMARY_KEY] in this_class.CACHE:
            return this_class.CACHE[args[this_class.PRIMARY_KEY]]

        model = this_class(**args)
        if not is_new:
            model.__updated__attr = {}
            if this_class.PRIMARY_KEY in args:
                model.__id = args[this_class.PRIMARY_KEY]
            model.set_parents_id()
            this_class.CACHE[model.__id] = model
        return model

class RolePermission(Model):
    DB = "db1"
    TABLE = 'auth_role_permission'
    
    def _attributtes(self):
        return {
            "id" : Model._integer(),
            "role" : Model._hasOne(Role, on={
                "id_role" : "id"
            }),
            "permission" : Model._hasOne(Permission, on={
                "id_permission" : "id"
            })
        }

class UserRolePermission(Model):
    DB = "db1"
    TABLE = 'auth_user_role_permission'

    def _attributtes(self):
        return {
            "id" : Model._integer(),
            "role" : Model._hasOne(Role, on={
                "id_role_permission" : "id"
            }),
            "permission" : Model._hasOne(Permission, on={
                "id_role_permission" : "id"
            })
        }
