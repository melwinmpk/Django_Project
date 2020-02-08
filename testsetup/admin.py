from django.contrib import admin
from .models import QuestionDefinition,SubjectDefinition
# Register your models here.

admin.site.register(QuestionDefinition)
admin.site.register(SubjectDefinition)
