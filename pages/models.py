from django.db import models
from django.conf import settings

# Create your models here.


class Apresentacao(models.Model):
    title = models.CharField("Título", max_length=100)
    text = models.TextField("Texto", null=False)
    background = models.ImageField("Background", null=False)
    
    class Meta:
        db_table = "apresentation"
    
    def __str__(self):
        return self.title
    

class Categorias(models.Model):
    nome = models.CharField("Categoria", max_length=100, null=False)
    descricao = models.TextField("Descrição", null=False)
    
    class Meta:
        db_table = "categorias"

    def __str__(self):
        return self.nome

class Posts(models.Model):
    title = models.CharField("Título", max_length=100, null=False)
    text = models.TextField("Texto", null=False)
    date = models.DateTimeField("Date", null=False, auto_now=True)
    banner = models.ImageField("Banner", null=False)
    
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return self.title


class Livros(models.Model):
    title = models.CharField("Título", max_length=100, null=False)
    author = models.CharField("Autor", max_length=100, null=False)
    banner = models.ImageField("Banner", null=False)
    descricao = models.TextField("Descrição", null=False)
    

    class Meta:
        db_table = "livros"

    def __str__(self):
        return self.title

class Config(models.Model):
    name = models.CharField("Nome do Blog", max_length=100, null=False, default="[Nome do Blog]")
    status = models.CharField("Status do Blog", max_length=100, null=False, default="[Status do Blog]")
    owner = models.CharField("Dono do Blog", max_length=100, null=False, default="[Dono do Blog]")
    year = models.IntegerField("Publicação", null=False, default="0000")

    class Meta:
        db_table = "configs"

    def __str__(self):
        return self.name

class Colors(models.Model):
    main = models.CharField("Main Color", max_length=10, null=False, default="#87ad93")
    strong = models.CharField("Main Color", max_length=10, null=False, default="#526e5b")
    neutral = models.CharField("Main Color", max_length=10, null=False, default="#cccccc")
    lighter = models.CharField("Main Color", max_length=10, null=False, default="#e6f8ec")
    
    class Meta:
        db_table = "colors"
    
    def __str__(self):
        return self.main