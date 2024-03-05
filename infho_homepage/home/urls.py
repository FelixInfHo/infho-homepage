from django.urls import path
from django.urls import re_path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog_overview, name="blog"),
    re_path(r"^blog/(?:post-(?P<blog_id>[0-9]+)/)?$", views.blog_entry, name="blog_post"),  # good
]
