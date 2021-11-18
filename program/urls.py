from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

from .views import program

urlpatterns = [
    path('', views.program, name="program"),

#    path('number_view/', views.number_view.as_view(), name="number_view"), 


]
