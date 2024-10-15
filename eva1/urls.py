from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),  # Única ruta que muestra el template con los valores
]
