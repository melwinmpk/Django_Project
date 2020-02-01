from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'), # HomeView
    path('login',views.login, name='index'),
    path('register',views.register, name='index')
]