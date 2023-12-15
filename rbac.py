class User:
    def __init__(self, name):
        self.name = name
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
