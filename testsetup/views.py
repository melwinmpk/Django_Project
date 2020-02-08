from django.shortcuts import render
from accounts.views import render_data
from django.http import JsonResponse
from testsetup.models import SubjectDefinition,QuestionDefinition

# Create your views here.
def createtest(request):
    return True

def createsubject(request):
    return render(request, 'subject.html', render_data('subject'))

def addQuestion(request):
    subjectsobj     = SubjectDefinition.objects.all()
    questionTypeobj = QuestionDefinition.objects.all()
    questionType = {}
    subjects = {}
    for entry in questionTypeobj.values():
        questionType[entry['id']] = entry['QuestionType']
    for entry in subjectsobj.values():
        subjects[entry['id']] = entry['SubjectName']
    # print(list_result)
        # list_result['subjects'][entry['id']] = entry['SubjectName']

    return render(request, 'questionAdd.html', render_data('questionAdd',{'questionType':questionType,'subjects':subjects}))