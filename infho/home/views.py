from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    return render(
            request, "home/index.html", {"request": request, "posts": Post.objects.order_by("-date")[:5]}
        )
