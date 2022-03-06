from django.db import models

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=50)
    description= models.CharField(max_length=50)
    
    def __str__(self):
        self.title