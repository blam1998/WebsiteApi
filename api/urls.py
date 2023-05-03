from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('updateTask/', views.putTask),
    path('addUser/', views.addUser)
]
