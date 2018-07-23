from django.contrib import admin
from .models import Project
# Register your models here.

# To make the model visible to the admin page
admin.site.register(Project)
