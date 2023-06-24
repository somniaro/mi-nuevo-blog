from django.urls import path #importa la función path de Django
from . import views # importa Views desde la aplicación blog

urlpatterns = [
    path('', views.post_list, name='post_list'),
]