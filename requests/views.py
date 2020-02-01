from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def controllers(request):
    if request.method == 'POST':
        mode = request.POST['mode']
        ack  = request.POST['ack']
        # call respective function.
        data = {}
    return JsonResponse(data)
    # return render(request, 'index.html', render_data('index'))