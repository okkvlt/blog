from django.contrib import admin
from sympy import Li

# Register your models here.
from .models import *

class ConfigList(admin.ModelAdmin):
    list_display = ("id", "name", "status", "owner", "year")
    
class ColorsList(admin.ModelAdmin):
    list_display = ("main", "strong", "neutral", "lighter")
    
class ApresentationList(admin.ModelAdmin):
    list_display = ("id", "title", "text", "background")

class CategoryList(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao")

class PostsList(admin.ModelAdmin):
    list_display = ("id", "title", "author", "date", "banner")
    
class LivrosList(admin.ModelAdmin):
    list_display = ("id", "title", "author", "descricao", "banner")

admin.site.register(Config, ConfigList)
admin.site.register(Apresentacao, ApresentationList)
admin.site.register(Colors, ColorsList)
admin.site.register(Categorias, CategoryList)
admin.site.register(Posts, PostsList)
admin.site.register(Livros, LivrosList)