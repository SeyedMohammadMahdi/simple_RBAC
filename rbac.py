class RBAC:
    def __init__(self):
        self.users = []
        self.roles = []
        self.objects = []
        self.add_user("admin", "admin")

    def add_user(self, name, password):
        self.users.append(User(name, password))

    def show_users(self):
        for i,j in enumerate(self.users):
            print(i, j)



class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.roles = []

    def add_role(self, roles):
        self.roles = roles

    def __str__(self):
        return self.name



class Object:
    def __init__(self, name, owner, content=""):
        self.name = name
        self.owner = owner
        self.content = content

    def write(self, new_content):
        self.content = new_content

    def read(self):
        print(self.content)



class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def __str__(self):
        print(self.name)
        print(self.permissions)
        return ""

if __name__ == "__main__":
    rbac = RBAC()
    state = 0
    while(True):
        if state == 0:
            user_name = input("enter usersname: ")
            password = input("enter password: ")

            for i in rbac.users:
                if user_name == i.name and password == i.password:
                    state = 1
                    break
        elif state == 1:
            print(0, "add user")
            print(1, "show users")
            opt = input("choose option: ")

