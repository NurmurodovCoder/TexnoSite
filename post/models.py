from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.html import format_html


class Post(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to="post/")
    text = RichTextField()  # text=CKEditor5Field('Text', config_name='extends')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default="Maxfiy mallif", null=True, blank=True
    )
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name="like")
    read = models.PositiveIntegerField(default=0)

    def show_image(self):
        return format_html(
            "<img src='{}' width='400' height='200' />".format(self.img.url)
        )

    show_image.short_description = "Image"

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="author/")
    bio = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60)
    img = models.ImageField(upload_to="category/")

    def __str__(self):
        return self.name


class Carusel(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="carusel/")
    body = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CommentPost(models.Model):
    text = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
