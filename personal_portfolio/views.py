from django.shortcuts import render
from personal_portfolio.models import Project
# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project':project}
    return render(request, 'project/project_detail.html', context)