"""profinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import projects, project, createProject, updateProject, deleteProject, projects_by_tag


urlpatterns = [
    path('', projects, name='projects'),
    path('project-object/<str:pk>/', project, name='project'),
    path('create-project/', createProject, name='create-project'),
    path('update-project/<str:pk>', updateProject, name='update-project'),
    path('delete-project/<str:pk>', deleteProject, name='delete-project'),
    path('tag/<slug:tag_slug>', projects_by_tag, name="tag"),
]
