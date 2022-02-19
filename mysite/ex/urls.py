from django.urls import path
from . import views
from django.http import HttpResponse
app_name = "example"
urlpatterns = [
    path('', views.index, name='index'),
]
