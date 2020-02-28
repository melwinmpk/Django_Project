from django.db import models

# Create your models here.

class QuestionDefinition(models.Model):
    QuestionTypeId = models.AutoField(auto_created = True,primary_key = True,serialize = False,null=False,default=None)
    QuestionType   = models.CharField(max_length=100,blank=True, null=True)

class SubjectDefinition(models.Model):
    SubjectName = models.CharField(max_length=100,blank=True, null=True)
    SubjectId   = models.AutoField(auto_created = True,primary_key = True,serialize = False,null=False,default=None)

class Questions(models.Model):
    # Subjectid  = models.CharField(max_length=100,default=1)
    # QuesType   = models.IntegerField(blank=False, null=False,default=1)
    SubjectId        = models.ForeignKey(SubjectDefinition,on_delete=models.CASCADE,default=None)
    Question         = models.CharField(max_length=320,blank=True, null=True)
    Options          = models.TextField(blank=True, null=True)
    QuestionTypeId   = models.ForeignKey(QuestionDefinition,on_delete=models.CASCADE,default=None)
    Ans              = models.IntegerField(blank=False, null=False)