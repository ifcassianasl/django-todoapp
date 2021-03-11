from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/item/', views.delete_item, name='delete_item'),
    path('delete/todo/', views.delete_todo, name='delete_todo'),
    path('check_item/', views.check_item, name='check_item'),
]
