from django.db import models
from django.core.validators import MinLengthValidator

from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
  author             = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                        #editable=False
                      )
  date              = models.DateTimeField("Datum des Beitrags")
  title             = models.CharField("Titel", max_length=128)
  photo             = models.ImageField("Bild zum Post", upload_to="blogbilder", null=True, blank=True)
  content           = models.TextField("der Beitrag", max_length=16384)
  slug              = models.SlugField(unique=True)
  photo1            = models.ImageField("Bild 1 zum Post", upload_to="blogbilder", null=True, blank=True)
  photo2            = models.ImageField("Bild 2 zum Post", upload_to="blogbilder", null=True, blank=True)
  photo3            = models.ImageField("Bild 3 zum Post", upload_to="blogbilder", null=True, blank=True)
  tags              = models.ManyToManyField(Tag)
  information       = models.BooleanField("reiner Informationspost", default=False)

  def __str__(self):
    return f"»{self.title}« ~ {self.author.last_name}, {self.author.first_name} ({self.author.username}) – {self.content[:min(len(self.content), 26)]}..."

  class Meta:
    verbose_name = "Blog Posting" 
    #permissions = (("manage_blog_posts", "erlaubt die Verwaltung von Blogposts"),)

class Kurs(models.Model):
  referenten       = models.ManyToManyField(get_user_model())
  title            = models.CharField("Titel", max_length=128, default="")
  description      = models.TextField("der Beitrag", max_length=16384)
  # ggf als eigenes Model
  Ort            = models.CharField("Ort", max_length=128, default="")

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")


