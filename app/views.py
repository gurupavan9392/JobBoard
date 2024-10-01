from django.shortcuts import render,get_list_or_404
from app.models import *
# Create your views here.

def job_list(request):
    jobs=Job.objects.all()
    return render(request,'job_list.html',{'jobs':jobs})

def job_detail(request,job_id):
    job=get_list_or_404(Job,pk=job_id)
    return render(request,'job_detail.html',{'job':job})