from django.db import models
from django.utils import timezone
# Create your models here.

class Project(models.Model):
    #   To get the user's name
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #   Give the project a name
    project_title = models.CharField(max_length=200)
    #   Give the project a brief description
    project_desc = models.TextField(max_length=500)
    #   Date when the project was created
    created_date = models.DateTimeField(default=timezone.now)
    #   Date when the project was last modified
    last_modified_date = models.DateTimeField(blank = True, null=True)

    def __str__(self):
        return self.project_title
