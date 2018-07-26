from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.utils import timezone
from .forms import ProjectForm, DocumentForm
# Create your views here.
def project_list(request):
    #   Projects are ordered by the date it was last modified
    projects = Project.objects.filter(last_modified_date__lte=timezone.now()).order_by('last_modified_date')
    return render(request, 'app/project_list.html', {'projects':projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'app/project_detail.html', {'project':project})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.last_modified_date = timezone.now()
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'app/project_edit.html', {'form':form})

def project_edit(request, pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid():
            project = form.save(commit = False)
            #project.username = request.user
            project.last_modified_date = timezone.now()
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance = project)
    return render(request, 'app/project_edit.html', {'form':form})

def project_add(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance = project)
        if form.is_vaild():
            form.save(commit = False)
            return redirect('project_detail', pk=project.pk)
    else:
        form = DocumentForm(instance = project)
    return render(request, 'app/addfile.html', {'form':form})
