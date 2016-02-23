from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Paintjob

# Create your views here.
def index(request):
    job_list = Paintjob.objects.order_by('-due_date')
    template = loader.get_template('paintjobs/index.html')
    context = {
        'job_list': job_list,
    }
    return HttpResponse(template.render(context, request))

def raise_e(request):
    raise Exception("In your face!")
    return HttpResponse("I raised an exception. This shouldn't be displayed.")

def oom(request):
    gig = 2**30 * b'A'
    return HttpResponse("I allocated 1GB of memory in this request. I shouldn't have been able to do that and live.")

def faffing(request):
    import time
    time.sleep(60*60)
    return HttpResponse("I slept for an hour in this request. I shouldn't have been able to do that and live.")
