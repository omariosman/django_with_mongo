from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

from .views import program

app_name = "program"


urlpatterns = [
    path('main_program/', views.program, name="program"),
    path('insert_program/', views.insert_program, name="insert_program"),
    path('type_instruction/', views.type_instruction, name="type_instruction"),
    path('execute_program/', views.execute_proram, name="execute_proram"),

    path('', views.base, name="base"),

#    path('number_view/', views.number_view.as_view(), name="number_view"), 

]
