from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', render_data('index'))

def login(request):
    data = {}
    # return JsonResponse(data)
    return render(request, 'login.html', render_data('login'))

def register(request):
    return render(request, 'register.html', render_data('register'))

def render_data(view):
    return {'title':view,'view_js':view+'.js','view_css':view+'.css'}