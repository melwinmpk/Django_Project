from django.shortcuts import render
from accounts.views import render_data
from django.http import JsonResponse
from testsetup.models import SubjectDefinition,QuestionDefinition,Questions
from requests.requestactions.testsetup import testsetup
import ast
import json

# Create your views here.
def createtest(request):
    return True

def createsubject(request):
    return render(request, 'subject.html', render_data('subject'))

def addQuestion(request):
    subjectsobj     = SubjectDefinition.objects.all()
    questionTypeobj = QuestionDefinition.objects.all()
    return render(request, 'questionAdd.html', render_data('questionAdd',{'questionType':questionTypeobj,'subjects':subjectsobj}))

def testselection(request):
    subjectsobj   = SubjectDefinition.objects.all()
    return render(request, 'testselection.html',render_data('testselection',{'subjects':subjectsobj}))

def taketest(request):
    subjectIds = ast.literal_eval(request.GET['subjectids'])
    subjectIds = [n.strip() for n in subjectIds]  # removes extra spaces
    objsubjectids = {'subjectids':[ i for i in subjectIds ]}
    questionobj = testsetup()
    data = questionobj.taketestAck(request,objsubjectids)

    return render(request,'taketest.html',render_data('taketest',{'subjectids':request.GET['subjectids'],'QuestionIds':data}))