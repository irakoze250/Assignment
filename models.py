from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=100)
    tech = models.TextField()
    pub_date = models.DateTimeField('publishing day')
    author = models.CharField(max_length=50)
    
    


