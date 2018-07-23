from django.shortcuts import render
from .models import Project
# Create your views here.
def project_list(request):
    #   Projects are ordered by the date it was last modified
    projects = Project.objects.filter(last_modified_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/project_list.html', {'projects':projects})
