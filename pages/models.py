from datetime import datetime

from django.conf import settings
from django.db import models

# Create your models here.


class Sobre(models.Model):
    title = models.CharField("Título", max_length=100, null=False)
    text = models.TextField("Texto", null=False)

    class Meta:
        db_table = "sobre"

    def __str__(self):
        return self.title


class Apresentacao(models.Model):
    title = models.CharField("Título", max_length=100)
    text = models.TextField("Texto", null=False)
    background = models.ImageField(
        "Background", null=False, upload_to="img/banners/")

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
    banner = models.ImageField("Banner", upload_to="img/posts/", null=False)

    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return self.title


class Livros(models.Model):
    title = models.CharField("Título", max_length=100, null=False)
    author = models.CharField("Autor", max_length=100, null=False)
    file = models.FileField("File", upload_to="pdf/", null=False)
    banner = models.ImageField("Banner", upload_to="img/books/", null=False)
    descricao = models.TextField("Descrição", null=False)

    class Meta:
        db_table = "livros"

    def __str__(self):
        return self.title


class Config(models.Model):
    name = models.CharField("Nome do Blog", max_length=100,
                            null=False, default="[Nome do Blog]")
    status = models.CharField(
        "Status do Blog", max_length=100, null=False, default="[Status do Blog]")
    owner = models.CharField(
        "Dono do Blog", max_length=100, null=False, default="[Dono do Blog]")
    year = models.IntegerField("Publicação", null=False, default="0000")
    logo = models.ImageField("Logo do Blog", upload_to="img/logos/", null=True)

    class Meta:
        db_table = "configs"

    def __str__(self):
        return self.name


class Colors(models.Model):
    main = models.CharField("Main Color", max_length=10,
                            null=False, default="#a74242")
    strong = models.CharField(
        "Strong Color", max_length=10, null=False, default="#661515")
    neutral = models.CharField(
        "Neutral Color", max_length=10, null=False, default="#cccccc")
    lighter = models.CharField(
        "Lighter Color", max_length=10, null=False, default="#f8cfcf")

    class Meta:
        db_table = "colors"

    def __str__(self):
        return self.main
