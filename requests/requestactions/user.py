from  django.contrib.auth.models import User,auth
from django.contrib import messages
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

    def loginAck(self,request):

        user = auth.authenticate(username=self.username, password=self.password)
        if user is not None:
            auth.login(user)
            return json.dumps({'status':'success'})
        else:
            messages.info(request, 'Invalid Credentials')
            return json.dumps({'status':'fail','error':'Invalid Credentials'})


    def registerAck(self):
        if User.objects.filter(username=self.username).exists():
            messages.info(request, 'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=self.emailid).exists():
            messages.info(request, 'email taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=self.username, password=password1, email=self.emailid, first_name=self.first_name,
                                            last_name=self.last_name)
            user.save();
            messages.info(request, 'UserId Created')
            return redirect('login')
