from django.db import models

# Create your models here.
class Questions(models.Model):

    Subject = models.CharField(max_length=100)
    Ques    = models.CharField(max_length=320)
    Op_1    = models.CharField(max_length=100)
    Op_2    = models.CharField(max_length=100)
    Op_3    = models.CharField(max_length=100)
    Op_4    = models.CharField(max_length=100)
    Ans     = models.IntegerField()

