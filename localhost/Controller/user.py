from Jati.Base.Controller import Controller

class user(Controller):
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

    def tes_query(self):
        tabel_user = self.Databases["db1"]['user']
        tabel_role = self.Databases["db1"]['auth_item']
        
        # select. output iter
        print('q1')
        users = tabel_user.select(('name', 'nama',), 'email')
        print(users)

        # select. output iter
        print('q2')
        roles = tabel_role.select()
        print(roles)

        # select. output iter
        print('q3 updating')
        user_updated = tabel_user.update({
            "name": "gupron"
        }, where=(('id', 1), ))
        print(user_updated)
        print('q3 updated')
        
        print('user_updated', user_updated)
        for u in user_updated:
            print("updated", u)

        print('roles', roles)
        for r in roles:
            print("role", r)
            
        print('rq1', users, users.query)
        g = users.__next__()
        print(g)
        for u in users:
            print("user", u)

        # select advace. output iter
        tabel_user.select('name', 'email', 'phone', 
            join=(('customer', 'c'), 'c.id_user = user.id'),
            where=[],
            group_by=(),
            having_by='where_query',
            order_by=()
        ).limit(1)

        # insert
        tabel_user.insert({
            "name": "Moh Gupron", 
            "email":"ghuvrons@gmail.com"
        })

        # asd
        tabel_user.delete(
            where=[]
        )
