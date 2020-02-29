from  django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
from testsetup.models import SubjectDefinition,Questions,QuestionDefinition
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
    questionid   = 0
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
        if "questionid" in data:
            self.questionid = data['questionid']




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
            SubjectId       = SubjectDefinition.objects.get(SubjectId=self.subjectid),
            Question        = self.Question,
            Options         = self.options,
            QuestionTypeId  = QuestionDefinition.objects.get(QuestionTypeId=self.questiontype),
            Ans             = self.Ans)
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
            # print(subjectid)
            Subject_questionid_list = list(Questions.objects.filter(SubjectId=subjectid).values_list('id'))

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

    def getquestiondataAck(self,request,questionid = None):
        self.userlogincheck()

        if questionid == None:
            questionid = self.questionid
            fromAjaxcall = True
        else:
            fromAjaxcall = False

        questiondata =  Questions.objects.filter(id=questionid)
        result = questiondata.values()  # return ValuesQuerySet object
        list_result = [entry for entry in result][0]
        if fromAjaxcall:
            return json.dumps({'status': 'success','data':list_result})
        else:
            return list_result

    def checkanswerAck(self,request):
        self.userlogincheck()
        question_ans = Questions.objects.filter(id=self.questionid).values_list('Ans')
        return json.dumps({'status': 'success', 'data': {'questionid':self.questionid,"Ans":list(question_ans)[0][0]}})
    def gettestquestionidsAck(self,request):
        self.userlogincheck()
        # request.session['questiontypes'] = QuestionDefinition.objects.all()  "QuestionTypes":request.session['questiontypes']
        # request.session['subjectdata'] = SubjectDefinition.objects.filter(SubjectId=request.GET['subjectids'])
        return json.dumps({'status': 'success', 'data': {'subjectids': request.session['subjectids'], "QuestionIds": request.session['QuestionIds'],"Subjectdata":request.session['subjectdata'],"QuestionTypes":request.session['questiontypes']}})
    def render_data(self,view, data=None):
        if data == None:
            return {'title': view, 'view_js': view + '.js', 'view_css': view + '.css'}
        else:
            return {'title': view, 'view_js': view + '.js', 'view_css': view + '.css', 'data': data}





