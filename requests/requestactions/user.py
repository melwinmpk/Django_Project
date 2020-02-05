from  django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
import json

class user:
    username = ''
    password = ''
    email  = ''
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
        if "email" in data:
            self.email = data['email']
        if "first_name" in data:
            self.first_name = data['first_name']
        if "last_name" in data:
            self.last_name = data['last_name']
        print("User Object Initilized ")
        # return self

    def loginAck(self,request):

        user = auth.authenticate(username=self.username, password=self.password)
        if user is not None:
            auth.login(request,user)
            # redirect('home')
            return json.dumps({'status':'success'})
            # return redirect('/home')
        else:
            messages.info(request, 'Invalid Credentials')
            return json.dumps({'status':'Fail','message':'Invalid Credentials'})


    def registerAck(self,request):
        if User.objects.filter(username=self.username).exists():
            return json.dumps({'status':'Fail','message':'Username Already exist try somthing else.'})
        elif User.objects.filter(email=self.email).exists():
            return json.dumps({'status':'Fail','message':'EmailId Already exist try somthing else.'})
        else:
            user = User.objects.create_user(username=self.username, password=self.password, email=self.email, first_name=self.first_name,
                                            last_name=self.last_name)
            user.save();
            redirect('/home')
            return json.dumps({'status':'success','message':'account created'})
