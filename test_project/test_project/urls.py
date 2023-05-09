"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from lists import views

urlpatterns = [
    path('home/', views.home_page, name="home"),
    path("file/", views.get_file, name="get_file"),
    path("load_exe/", views.load_excel_file_exe, name="load_excel_file.exe"),
    path("load_excel/", views.load_excel_file, name = "load"),
    path("load_apk/", views.load_apk_file, name = "apk"),
    path('list/', views.Items_list.as_view()),
    path('one/', views.One_item.as_view())
] 
