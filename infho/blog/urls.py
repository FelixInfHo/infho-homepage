from django.urls import path

from blog import views

urlpatterns = [
    path("", views.index, name="blog-page"),
    path('post/<slug:slug>/', views.post, name='post-detail-page')
]
