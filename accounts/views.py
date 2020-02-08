from django.shortcuts import render
from  django.contrib.auth.models import User,auth
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', render_data('index'))

def login(request):
    data = {}
    # return JsonResponse(data)
    return render(request, 'login.html', render_data('login'))
def logout(request):
    auth.logout(request)
    return render(request, 'index.html', render_data('index'))

def register(request):
    return render(request, 'register.html', render_data('register'))

def render_data(view,data = None):
    if data == None:
        return {'title':view,'view_js':view+'.js','view_css':view+'.css'}
    else:
        return {'title':view,'view_js':view+'.js','view_css':view+'.css','data':data}