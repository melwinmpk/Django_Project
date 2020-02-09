from  django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
from testsetup.models import SubjectDefinition
import json


class testsetup:
    subjectname  = ''
    questiontype = 1
    Question     = ''
    options      = {}
    def userlogincheck(self):
        print("userlogin check calling respective function")
    def __init__(self,data):
        data = json.loads(data)
        if "subjectname" in data:
            self.subjectname = data['subjectname']
        if "questiontype" in data:
            self.questiontype = data['questiontype']
        if "Question" in data:
            self.Question = data['Question']
        if "options" in data:
            self.options = data['options']


    # @userlogincheck
    def savesubjectAck(self,request):
        self.userlogincheck()
        subjaectobj = SubjectDefinition(SubjectName = self.subjectname)
        subjaectobj.save()
        return json.dumps({'status':'success'})

    def savequestionAck(self,request):
        print(request)
        return json.dumps({'status':'success'})





