from django.conf.urls import url, include
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^server/', views.ServerView.as_view()),
    # url(r'^index/', views.IndexView.as_view()),
]