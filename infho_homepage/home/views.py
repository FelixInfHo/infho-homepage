from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
            request, "title_page/index.html", {"movie": "Casablanca", "year": 1942}
        )
