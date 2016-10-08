from django.shortcuts import render

# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogPost

def blog(request):
	posts = BlogPost.objects.all()
	t = loader.get_template("blog.html")
	c = Context({'posts':posts})
	return HttpResponse(t.render(c))