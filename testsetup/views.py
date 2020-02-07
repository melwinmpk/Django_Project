from django.shortcuts import render
from accounts.views import render_data
from django.http import JsonResponse

# Create your views here.
def createtest(request):
    return True

def createsubject(request):
    return render(request, 'subject.html', render_data('subject'))