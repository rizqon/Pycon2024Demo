from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('del/<int:todo_id>/delete', views.delete, name='delete'),
]