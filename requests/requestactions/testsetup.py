from  django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
from testsetup.models import SubjectDefinition,Questions
import json
import base64


class testsetup:
    subjectname  = ''
    questiontype = 1
    Question     = ''
    options      = {}
    Ans          = 1
    subjectid    = 1
    def userlogincheck(self):
        print("userlogin check calling respective function")
    def __init__(self,data):
        data = json.loads(data)
        if "subjectname" in data:
            self.subjectname = data['subjectname']
        if "subjectid" in data:
            self.subjectid = data['subjectid']
        if "questiontype" in data:
            self.questiontype = data['questiontype']
            if int(self.questiontype) == 1:
                if "options" in data:
                    self.options = data['options']
        if "Question" in data:
            self.Question = data['Question']
        if "Ans" in data:
            self.Ans = int(data['Ans'])



    # @userlogincheck
    def savesubjectAck(self,request):
        if self.subjectname != None and self.subjectname != '':
            self.userlogincheck()
            subjaectobj = SubjectDefinition(SubjectName = self.subjectname)
            subjaectobj.save()
            return json.dumps({'status':'success'})
        else:
            return json.dumps({'status': 'fali','message':'data subjectname missing'})
    def savequestionAck(self,request):
        self.userlogincheck()
        questionobj = Questions(
            Subjectid = self.subjectid,
            Question  = self.Question,
            Options   = self.options,
            QuesType  = self.questiontype,
            Ans       = self.Ans)
        questionobj.save()
        return json.dumps({'status':'success'})





