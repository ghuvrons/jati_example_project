from Jati.ErrorHandler import WSError

class isAdmin():
    def run(self, **kw):
        auth = kw['auth']
        if not auth.user:
            raise WSError((511, 'who are you?', ))
        return True