from django.urls import path
from . import views

app_name = 'countries'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('all/', views.all, name='all'),
    path('modify/<int:id>/', views.modify, name='modify'),
    path('', views.home, name='home'),
]


