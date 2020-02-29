from django.shortcuts import render
from accounts.views import render_data
from testsetup.models import SubjectDefinition,QuestionDefinition
from requests.requestactions.testsetup import testsetup
import ast

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
    questionid_data = {}
    for subject in data:
        for questionid in data[subject]:
            questionid_data = questionobj.getquestiondataAck(request,questionid)
            questionid_data['Options'] = ast.literal_eval(questionid_data['Options'])
            questionid_data['Options'] = [n.strip() for n in questionid_data['Options']]  # removes extra spaces
            questionid_data['Options'] = [i for i in questionid_data['Options']]
            break
        break

    subjectdefinition = SubjectDefinition.objects.filter(SubjectId__in=objsubjectids['subjectids']).values()
    list_result = {entery['SubjectId'] :  entery for entery in subjectdefinition }
    request.session['subjectdata'] = list_result
    questiondefinition = QuestionDefinition.objects.all().values()
    list_result1       = {entery['QuestionTypeId']: entery for entery in questiondefinition}

    request.session['subjectids']        = request.GET['subjectids']
    request.session['QuestionIds']       = data
    request.session['questiontypes']     = list_result1
    questionid_data['SubjectId_id']      = list_result[questionid_data['SubjectId_id']]['SubjectName']
    questionid_data['QuestionTypeId_id'] = list_result1[questionid_data['QuestionTypeId_id']]['QuestionType']

    return render(request,'taketest.html',render_data('taketest',{'subjectids':request.GET['subjectids'],'QuestionIds':data,'questiondata':questionid_data}))