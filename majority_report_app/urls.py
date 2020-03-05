#Defines URL patterns for majority_report_apps

from django.urls import path

from . import views

app_name = 'majority_report_app'
urlpatterns = [
    #Home Page
    path('',views.index, name = "index"),
    #Enviornment Form Page
    path('enviornment_variables/', views.env_forms, name = "variables"),
    path('results/<int:env_id>/', views.results, name = "results"),
    
]
