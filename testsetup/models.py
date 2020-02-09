from django.db import models

# Create your models here.
class Questions(models.Model):
    Subjectid  = models.CharField(max_length=100,default=1)
    Question   = models.CharField(max_length=320,blank=True, null=True)
    Options    = models.BinaryField(blank=True, null=True)
    QuesType   = models.IntegerField(blank=False, null=False,default=1)
    Ans        = models.IntegerField(blank=False, null=False)

class QuestionDefinition(models.Model):
    # QuestionTypeId = models.IntegerField(blank=False, null=False,unique=True)
    QuestionType   = models.CharField(max_length=100,blank=True, null=True)

class SubjectDefinition(models.Model):
    SubjectName = models.CharField(max_length=100,blank=True, null=True)
    # SubjectId   = models.IntegerField(blank=False, null=False,unique=True)

