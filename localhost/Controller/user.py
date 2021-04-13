from Jati.Base.Controller import Controller

class user(Controller):
    Services = {}
    Models = {}
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

    def tes_query(self):
        tabel_user = self.Databases["db1"]['user']
        
        # select. output iter
        tabel_user.select('name', 'email', 'phone', 
            join=(('customer', 'c'), 'c.id_user = user.id'),
            where=[],
            group_by=(),
            having_by='where_query',
            order_by=()
        ).limit(1)

        # insert
        tabel_user.insert({
            name: "Moh Gupron", 
            email:"ghuvrons@gmail.com"
        })

        # update
        tabel_user.update(
            {},
            where=[]
        )

        # asd
        tabel_user.delete(
            where=[]
        )
