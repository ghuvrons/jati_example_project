from Jati.Base.Controller import Controller

class test(Controller):
    Services = {}
    Models = {}
    Databases = {}
    def index(self):
        return "Hello World"

    def list_user(self, **kw):
        user = self.Models["user"]
        users = user.search().limit(2)
        results = []
        for u in users:
            results.append(u)
        return results

    def detail(self, **kw):
        user = self.Models["user"]
        user = user.one()
        return user

    def list_role(self):
        user = self.Models["user"]
        users = user.all()
        for u in users:
            print("user ", u.name)
            print("\troles", [(r.name, r.parents_id) for r in u.roles])
            print("\tpermi", [(p.name, p.parents_id) for p in u.permissions])
        print(self.Models["auth.role"].CACHE)
        return True

    def mongo_query(self):
        tabel_user = self.Databases["db2"]['user']
        
        # select. output iter
        print('q1')
        users = tabel_user.select({"name": {"$eq": "ghuvrons"}})
        print(users)

        for u in users:
            print("user", u)
        
        # insert
        users = tabel_user.insert({"name": "ghuvrons"})
        print(type(users), users)

        users = tabel_user.update({"$set": {"email": "ghuvrons@gmail.com"}}, {"name": {"$eq": "ghuvrons"}})
        print(users)

        return 