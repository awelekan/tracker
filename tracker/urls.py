from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_food/', views.add_food, name='add_food'),
    path('add_consume/', views.delete_consumed, name='add_consume'),
    path('delete_food/<int:pk>/', views.delete_food, name='delete_food'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
     path('signup/', views.signup, name='signup'),
]
