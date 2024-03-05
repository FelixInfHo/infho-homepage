from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost, InfoPost
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(
            request, "title_page/index.html", {"info_posts": InfoPost.objects.order_by("-pub_date")[:5]}
        )

def blog_overview(request):
    return render(
            request, "blog/blog_overview.html", {"blog_posts": BlogPost.objects.order_by("-pub_date")[:5]}
        )

def blog_entry(request, blog_id):
    return render(
            request, "blog/blog_view.html", {"blog_post": get_object_or_404(BlogPost, id=blog_id)}
        )

