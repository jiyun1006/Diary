from django.urls import path
from . import views

urlpatterns = [

    path('', views.list_article,name='list'),
    path('create/', views.create_article, name='create'),
    path('<int:pk>/', views.detail_article, name='detail'),
]
