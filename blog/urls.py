from . import views # . means current directory
from django.urls import path # to create url pattern

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name = 'blog_view'), # '<slug:slug>' is the pattern - when the user goes to a certain url eg. example.com/dogs, django will search in the slug column for dogs and when it finds it will execute BlogView
    path('about/', views.AboutView.as_view(), name = 'about_view'),
    path('', views.PostList.as_view(), name = 'home_view')
]