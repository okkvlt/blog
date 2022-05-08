import base64
import os
from io import BytesIO

from blog.settings import BASE_DIR
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image

from pages.models import *
from pages.utils import utils

# Create your views here.

def index(request):
    db_configs = Config.objects.get(id=1)
    db_owner = User.objects.get(username='occvlt')
    db_posts = Posts.objects.order_by("-id")[0:3]
    
    posts = []
    
    for post in db_posts: 
        posts.append([post.id, 
                      post.title, 
                      post.text, 
                      post.banner, 
                      post.date, 
                      post.author.first_name])
           
    site = {
        "blog_name": db_configs.blog_name,
        "blog_status": db_configs.blog_status,
        "year": db_configs.year,
        "owner": db_owner.get_full_name(),
        "posts": posts,
    }
    
    return render(request, "index.html", site)
