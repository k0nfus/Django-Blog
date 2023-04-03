from django.db import models
from django.urls import reverse
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Blog Image')
    slug = models.SlugField(null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    einleitung = models.CharField(max_length=250, null=True, blank=True)
    
    class Meta:
        ordering = ["-date",]
        verbose_name_plural = "Blogbeiträge"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=400, verbose_name="Kommentar")
    author = models.CharField(max_length=40, verbose_name="Name")
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-date",]
        verbose_name_plural = "Kommentare"
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("post_detail")