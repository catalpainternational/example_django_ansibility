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
