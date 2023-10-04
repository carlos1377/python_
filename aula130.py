# method vs @classmethod vs @staticmethod
# method - self, método da instância
# @classmethod - cls, método da classe
# @staticmethod - método estático(sem self, nem cls)

# se eu preciso de um self, é método de instância

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.passowrd = None

    def set_user(self, user):  # setter
        self.user = user

    def set_password(self, password):
        self.passowrd = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.passowrd = password
        return connection

    @staticmethod
    def log(msg):
        print('Log:', msg)


# c1 = Connection()
c1 = Connection.create_with_auth('carlos', '232241')
print(c1.user)
Connection.log('log static')
# c1.set_user('carlos')
# c1.set_password('123424')
print(vars(c1))
