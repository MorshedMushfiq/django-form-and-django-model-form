from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    email =  models.EmailField(null=True)
    dept =  models.TextField(null=True)
    
    def __str__(self):
        return f"{self.name}"