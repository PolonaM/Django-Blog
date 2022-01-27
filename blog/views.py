from django.shortcuts import render
from .models import Post #The . is a shortcut that tells it to search in the current package before the rest of the PYTHONPATH. So, if a same-named module Recipe exists somewhere else in your PYTHONPATH, it won't be loaded.
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView): #this class connects the model with a template, it inherits from the specialized view class
    model = Post # here we map {{object.title}},... in the blog.html to the model Post
    template_name = 'blog.html'

class AboutView(generic.TemplateView): # TemplateView does not require a model
    template_name = 'about.html' # here we don't have bodel since we have static html

class PostList(generic.ListView): #specialized in rendering multiple data rows (multiple posts)
    queryset = Post.objects.filter(status = 1).order_by('-date_created') # - means that the latest post will be on the top of the page and the oldest post at the bottom of the home page
    template_name = 'index.html'
