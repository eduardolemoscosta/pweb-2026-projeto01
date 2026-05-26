from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('equipe/', views.equipe, name='equipe'),
    path('sobre/', views.sobre, name='sobre'),
]
