from django.contrib import admin
from django.urls import path,include
from about import views

urlpatterns = [
    path('',views.home)
]