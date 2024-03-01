from django.db import models
from django.conf import settings
from django.contrib import admin

# Create your models here.
     

class PostingStore(models.Model):
  author           = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                        #editable=False
                      )
  pub_date         = models.DateTimeField("Datum des Beitrags")
  title            = models.CharField("Titel", max_length=128)
  title_image_path = models.CharField("URL zum Titelbild", max_length=512)
  content_text     = models.TextField("der Beitrag", max_length=16384)

  def __str__(self):
    return f"»{self.title}« ~ {self.author.last_name}, {self.author.first_name} ({self.author.username}) – {self.content_text[:26]}..."
  
class BlogPost(PostingStore):
  image_path_array = models.CharField(max_length=4096, default="")

  class Meta:
    verbose_name = "Blog Posting"
    #permissions = (("manage_blog_posts", "erlaubt die Verwaltung von Blogposts"),)

class InfoPost(PostingStore):
  
  class Meta:
    verbose_name = "Informationspost"
    #permissions = (("manage_information_posts", "erlaubt die Verwaltung von Informationen auf der Startseite"),)
