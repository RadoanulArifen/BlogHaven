from django.urls import path
from .import views


urlpatterns = [
    path('blogs/',views.blog_list,name='blog_list')
]
