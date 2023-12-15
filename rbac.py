# permissions [read, write, delete, create_user, delete_user, create_role]

class RBAC:
    def __init__(self):
        self.users = []
        self.roles = []
        self.objects = []
        self.loggedin = None
        self.add_user("admin", "admin")
        self.add_role("admin", ["read", "write", "delete", "create_user", "delete_user", "create_role"])
        self.users[0].add_role(self.roles[0])
        

    def add_user(self, name, password):
        self.users.append(User(name, password))

    def show_users(self):
        for i,j in enumerate(self.users):
            print(i, j)

    def add_role(self, name, permissions):
        self.roles.append(Role(name, permissions))

    def check_permission(self, permission):

        for i in self.loggedin.roles:
            if permission in i.permissions:
                return True
        
        return False


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.roles = []

    def add_role(self, role):
        self.roles.append(role)

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
                    rbac.loggedin = i
                    break

        elif state == 1:
            print(0, "add user")
            print(1, "show users")
            print(9, "logout")
            print(10, "exit")            

            opt = input("choose option: ")

            if opt == "0":
                state = 2
            elif opt == "1":
                state = 3
            elif opt == "9":
                state = 9
            else:
                state = exit
            

        elif state == 2:
            if rbac.check_permission("create_user"):
                user_name = input("enter user name: ")
                password = input("enter password: ")
                rbac.add_user(user_name, password)
                state = 1

            else:
                print("only admin can add user\n\n")
                state = 1

        elif state == 3:
            rbac.show_users()
            print("\n\n")
            state = 1

        elif state == 9:
            rbac.loggedin = None
            state = 0

        else:
            break
