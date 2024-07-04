from django.db import models

# Create your models here.



class Task(models.Model):

    Priority ={
        'low': "Low",
        'medium':'Medium',
        'high': 'High'
    }
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=33)
    created_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    Priority = models.CharField(choices=Priority, max_length=33)

    def __str__(self) -> str:
        return self.name
    



    

    