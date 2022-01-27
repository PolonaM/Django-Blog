from . import views # . means current directory
from django.urls import path # to create url pattern

urlpatterns = [
    path('', views.translator_view, name = 'translator_view') #we don't need as_view() since translator_view is already a function
]