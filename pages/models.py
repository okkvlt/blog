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
    date = models.DateTimeField("Date", null=False)
    banner = models.ImageField("Banner", null=False)
    
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return self.title


class Livros(models.Model):
    title = models.CharField("Título", max_length=100)
    author = models.CharField("Autor", max_length=100)
    banner = models.ImageField("Banner", null=False)

    class Meta:
        db_table = "livros"

    def __str__(self):
        return self.title

class Config(models.Model):
    name = models.CharField("Nome do Blog", max_length=100, null=False, default="[Nome do Blog]")
    status = models.CharField("Status do Blog", max_length=100, null=False, default="[Status do Blog]")
    owner = models.CharField("Dono do Blog", max_length=100, null=False, default="[Dono do Blog]")
    year = models.IntegerField("Publicação", null=False, default="0000")
    color = models.CharField("Cor", max_length=100, null=False, default="#87ad93")

    class Meta:
        db_table = "configs"

    def __str__(self):
        return self.name
