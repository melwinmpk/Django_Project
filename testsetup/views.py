from django.shortcuts import render
from accounts.views import render_data
from django.http import JsonResponse
from testsetup.models import SubjectDefinition,QuestionDefinition,Questions

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