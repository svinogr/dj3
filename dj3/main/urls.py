from django.urls import path
from . import views

urlpatterns = [
    path('group/', views.group, name='group'),
    path('', views.index, name='index'),
    path('group/<int:slug>', views.DetailView.as_view())
]
