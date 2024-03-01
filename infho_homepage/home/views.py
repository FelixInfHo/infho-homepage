from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost, InfoPost

# Create your views here.
def index(request):
    return render(
            request, "title_page/index.html", {"info_posts": InfoPost.objects.order_by("-pub_date")[:5]}
        )

def blog(request):
    return render(
            request, "title_page/blog.html", {"blog_posts": BlogPost.objects.order_by("-pub_date")[:5]}
        )

