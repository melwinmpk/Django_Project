from django.contrib import admin
from .models import QuestionDefinition,SubjectDefinition,Questions
# Register your models here.

admin.site.register(QuestionDefinition)
admin.site.register(SubjectDefinition)
admin.site.register(Questions)