from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('nuevo/', views.crear, name='crear'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
]
