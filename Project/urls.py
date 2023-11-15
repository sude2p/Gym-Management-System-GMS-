from django.urls import path
from .views import *

urlpatterns = [
    path('project/all/', projectView, name='home'),
    path('create/', projectAdd, name='project-create'),
    path('view/<int:pk>/', projectIdView, name='project-view'),
    path('edit/<int:pk>/', projectUpdate, name='project-edit'),
    path('delete/<int:pk>/', projectDelete, name='project-delete'),
    # path('usercount/', userCount, name='usercount')
]