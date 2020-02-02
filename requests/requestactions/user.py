import json

class user:
    username = ''
    password = ''
    emailid  = ''
    first_name = ''
    last_name = ''

    def __init__(self,data):
        data = json.loads(data) # type is dict
        print(type(data))
        # elem in LIST
        if "username" in data:
            self.username = data['username']
        if "password" in data:
            self.password = data['password']
        if "emailid" in data:
            self.emailid = data['emailid']
        if "first_name" in data:
            self.first_name = data['first_name']
        if "last_name" in data:
            self.last_name = data['last_name']
        print("User Object Initilized ")
        # return self
    def assignData(self,data):
        data = json.loads(data) # type is dict
        print(type(data))
        # elem in LIST
        if "username" in data:
            self.username = data['username']
        if "password" in data:
            self.password = data['password']
        if "emailid" in data:
            self.emailid = data['emailid']
        if "first_name" in data:
            self.first_name = data['first_name']
        if "last_name" in data:
            self.last_name = data['last_name']
        print("User Object Initilized ")
    def loginAck(self):
        # print(data)
        print("Add Function Called")
        data = {
            "username": self.username,
            "password": self.password,
        }
        data = json.dumps(data)
        return data
        # return True

    def registerAck(self):
        print("Swim faster")
