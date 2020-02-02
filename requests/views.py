from django.shortcuts import render
from django.http import JsonResponse
# from requests.requestactions.user import *
import json
from importlib import import_module
# Create your views here.
def controllers(request):
    if request.method == 'POST':
        mode     = request.POST['mode']
        ack      = request.POST['ack']
        username = request.POST['username']
        password = request.POST['password']
        # call respective function.

        # print(mode,ack,username,password)
        data = {
            "mode": mode,
            "ack":ack,
            "username":username,
            "password":password,
        }
        data         =  json.dumps(data)
        target_class = dynamic_import(mode, ack, data)
        controller   = target_class(data)
        data         = getattr(controller, ack + 'Ack')()


    return JsonResponse(json.loads(data), status=201)
    # return render(request, 'index.html', render_data('index'))

def dynamic_import(mode, ack, data):
    module_object = import_module('requests.requestactions.' + mode)
    target_class = getattr(module_object, mode)
    return target_class