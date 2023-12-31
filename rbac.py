# permissions [read, write, delete, create_user, delete_user, create_role]
permission = ["create", "read", "write", "delete", "create_user", "delete_user", "create_role", "assign_role", "delete_role"]

class RBAC:
    def __init__(self):
        self.users = []
        self.roles = []
        self.objects = []
        self.loggedin = None
        self.add_user("admin", "admin")
        self.add_role("admin", permission)
        # self.users[0].add_role(self.roles[0])
        self.assign_role(0, [0])
        

    def add_user(self, name, password):
        self.users.append(User(name, password))

    def show_users(self):
        for i,j in enumerate(self.users):
            print(i, j)

    def add_role(self, name, permissions):
        self.roles.append(Role(name, permissions))

    def assign_role(self, user_num, roles):
        for role in roles:
            self.users[user_num].add_role(self.roles[role])

    def delete_user(self, user_num):
        self.users.pop(user_num)

    def delete_role(self, role_num):
        role = self.roles[role_num]
        self.roles.pop(role_num)
        for user in self.users:
            if role in user.roles:
                user.roles.remove(role)
    def show_roles(self):
        for role in rbac.roles:
                print(role)

    def add_object(self, name):
        self.objects.append(Object(name))

    def show_object(self):
        for i, obj in enumerate(self.objects):
            print(i, obj)

    def delete_object(self, object_num):
        self.objects.pop(object_num)

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
        string  = self.name + ": [ "
        for role in self.roles:
            string += role.name + ", "
        string += " ]"
        return string
 


class Object:
    def __init__(self, name, content=""):
        self.name = name
        # self.owner = owner
        self.content = content

    def write(self, new_content):
        self.content = new_content

    def read(self):
        print(self.content)
    
    def __str__(self):
        return self.name


class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def __str__(self):
        # print(self.name)
        # print(self.permissions)
        return self.name + ": [ " + ", ".join(self.permissions) + " ]"



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
            print(2, "show roles")
            print(3, "add role")
            print(4, "assign role")
            print(5, "delete user")
            print(6, "delete role")
            print(7, "add object")
            print(8, "show objects")
            print(9, "write object")
            print(10, "read object")
            print(11, "delete object")
            print(12, "logout")
            print(13, "exit")            

            opt = input("choose option: ")

            if opt == "0":
                state = 2
            elif opt == "1":
                state = 3
            elif opt == "2":
                state = 4
            elif opt == "3":
                state = 5
            elif opt == "4":
                state = 6
            elif opt == "5":
                state = 7
            elif opt == "6":
                state = 8
            elif opt == "7":
                state = 9
            elif opt == "8":
                state = 10
            elif opt == "9":
                state = 11
            elif opt == "10":
                state = 12
            elif opt == "11":
                state = 13
            elif opt == "12":
                state = 14
            else:
                state = "exit"
            

        elif state == 2:
            if rbac.check_permission("create_user"):
                user_name = input("enter user name: ")
                password = input("enter password: ")
                rbac.add_user(user_name, password)
                state = 1

            else:
                print("permission denied\n\n")
                state = 1

        elif state == 3:
            rbac.show_users()
            print("\n\n")
            state = 1

        elif state == 4:
            rbac.show_roles()
            
            print()
            state = 1
        elif state == 5:
            if rbac.check_permission("create_role"):
                name = input("eneter role name: ")
                for i, j in enumerate(permission): 
                    print(i, j)
                print()
                permissions = input("eneter permissions number: ").split(" ")
                permissions = [int(i) for i in permissions]
                permissions = [permission[i] for i in permissions]
                rbac.add_role(name, permissions)
                print()
            else:
                print("permission denied\n")
            state = 1

        elif state == 6:
            if rbac.check_permission("assign_role"):
                for i, user in enumerate(rbac.users):
                    if i == 0:
                        continue
                    print(i, user.name)
                print()

                user_num = int(input("enter user number: "))
                for i, role in enumerate(rbac.roles):
                    print(i, role)
                print()
                roles = input("eneter roles number: ").split(" ")
                roles = [int(i) for i in roles]
                # roles = [rbac.roles[i] for i in roles]
                rbac.assign_role(user_num, roles)
            else:
                print("permission denied")
            print()
            state = 1
        
        elif state == 7:
            if rbac.check_permission("delete_user"):
                for i, user in enumerate(rbac.users):
                    if i == 0:
                        continue
                    print(i, user.name)
                print()

                user_num = int(input("enter user number: "))
                rbac.delete_user(user_num)
            else:
                print("permission denied")
            print()
            state = 1
        elif state == 8:
            if rbac.check_permission("delete_role"):
                for i, role in enumerate(rbac.roles):
                    if i == 0:
                        continue
                    print(i, role)
                print()

                role_num = int(input("eneter role num: "))
                rbac.delete_role(role_num)
            else:
                print("permission denied")
            print()
            state = 1
        
        elif state == 9:
            if rbac.check_permission("create"):
                name = input("eneter object name: ")
                rbac.add_object(name)
            else:
                print("permission denied")
            print()
            state = 1
        
        elif state == 10:
            rbac.show_object()
            print()
            state = 1
        
        elif state == 11:
            if (rbac.check_permission("write")):
                rbac.show_object()
                print()
                object_num = int(input("enter object num: "))
                content = input("enter content: ")
                rbac.objects[object_num].write(content)
            else:
                print("permission denied")
            
            print()
            state = 1
        
        elif state == 12:
            if (rbac.check_permission("read")):
                rbac.show_object()
                object_num = int(input("enter object num: "))
                print(rbac.objects[object_num].content)
            else:
                print("permission denied")
            print()
            state = 1
        
        elif state == 13:
            if rbac.check_permission("delete"):
                rbac.show_object()
                print()
                object_num = int(input("enter object num: "))
                rbac.delete_object(object_num)
            else:
                print("permission denied")
            
            print()
            state = 1

        elif state == 14:
            rbac.loggedin = None
            state = 0

        else:
            break
