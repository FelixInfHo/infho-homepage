from django.urls import path

from blog import views as blogviews
from . import views as startviews
urlpatterns = [
    path("", startviews.index, name="starting-page"),
    #path("posts", views.PostListView.as_view(), name="posts-page"),
    #path('post/<slug:slug>/', views.SinglePostView.as_view(), 
    #     name='post-detail-page')
]
