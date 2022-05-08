from django.contrib import admin
from sympy import Li

# Register your models here.
from .models import *

class ConfigList(admin.ModelAdmin):
    list_display = ("name", "status", "owner", "year", "color")

class CategoryList(admin.ModelAdmin):
    list_display = ("nome", "descricao")

class PostsList(admin.ModelAdmin):
    list_display = ("title", "author", "banner")
    
class LivrosList(admin.ModelAdmin):
    list_display = ("title", "author")

admin.site.register(Config, ConfigList)
admin.site.register(Categorias, CategoryList)
admin.site.register(Posts, PostsList)
admin.site.register(Livros, LivrosList)