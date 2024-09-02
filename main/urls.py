from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name= 'home2'),
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
    path('<int:id>', views.list, name= 'List'),
    path('delete/', views.dele, name= 'Delete')
]