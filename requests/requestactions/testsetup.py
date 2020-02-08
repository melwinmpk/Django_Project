from  django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
from testsetup.models import SubjectDefinition
import json


class testsetup:
    subjectname =''

    def userlogincheck(self):
        print("userlogin check calling respective function")
    def __init__(self,data):
        data = json.loads(data)
        if "subjectname" in data:
            self.subjectname = data['subjectname']

    # @userlogincheck
    def savesubjectAck(self,request):
        self.userlogincheck()
        subjaectobj = SubjectDefinition(SubjectName = self.subjectname)
        subjaectobj.save()
        return json.dumps({'status':'success'})





