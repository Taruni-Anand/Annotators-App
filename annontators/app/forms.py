from django import forms
from .models import Project
from .models import Document

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'project_desc', 'username',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)
