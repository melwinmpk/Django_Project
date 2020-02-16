from  django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
from testsetup.models import SubjectDefinition,Questions
import json
import random
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
    def __init__(self,data=None):
        if data == None:
            return
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

    def taketestAck(self,request,data=None):
        self.userlogincheck()
        subject_question_list = {}
        subjectid_data = {}
        fromAjaxcall = True
        if data == None:
            subjectid_data = json.loads(self.subjectid)
        else:
            fromAjaxcall = False
            subjectid_data = data['subjectids']

        for subjectid in subjectid_data:
            Subject_questionid_list = list(Questions.objects.filter(Subjectid=subjectid).values_list('id'))

            if len(Subject_questionid_list) > 0 :
                randomIds = self.randomgenerator(len(Subject_questionid_list) - 1)
                questionIds = []
                i = 0
                for index in randomIds:
                    print(index)
                    questionIds.append(Subject_questionid_list[index][0])
                    i+=1
                subject_question_list[str(subjectid)] = questionIds
        if fromAjaxcall:
            return json.dumps({'status': 'success','data':subject_question_list})
        else:
            print(subject_question_list)
            return subject_question_list

    def randomgenerator(self,Subject_question_len):
        subjectIds = []
        i = 0
        # Subject_question_len = Subject_question_len1
        print(Subject_question_len)
        while True:
            index = random.randint(0, Subject_question_len)
            if index not in subjectIds:
                subjectIds.append(index)
                i += 1
            if i >= 5 or (Subject_question_len < 5 and i >= (Subject_question_len)):
                break

        return subjectIds

    def render_data(self,view, data=None):
        if data == None:
            return {'title': view, 'view_js': view + '.js', 'view_css': view + '.css'}
        else:
            return {'title': view, 'view_js': view + '.js', 'view_css': view + '.css', 'data': data}





