from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Paintjob
import time
import sys

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

def oom(request, mb='512'):
    mb = int(mb)
    blob = bytearray(mb * 2**20)
    return HttpResponse("I allocated %d MB of memory in this request." % mb)

def faffing(request, duration='3600'):
    duration = float(duration)
    time.sleep(duration)
    return HttpResponse("I slept for %d seconds in this request." % duration)

def shoutstdout(request, text="Hurray for STDOUT!"):
    print(text, file=sys.stdout)
    sys.stdout.flush()
    return HttpResponse("I wrote '%s' to stdout and flushed." % text)

def shoutstderr(request, text="Hurray for STDERR!"):
    print(text, file=sys.stderr)
    sys.stderr.flush()
    return HttpResponse("I wrote '%s' to stderr and flushed." % text)
