from django.urls import path
from . import views
from .views import PostsListView, PostsDetailView, PostsCreateView, PostsUpdateView, PostsDeleteView, UserPostListView

urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='userPosts'),
    path('blog/<int:pk>', PostsDetailView.as_view(), name='postDetail'),
    path('blog/new', PostsCreateView.as_view(), name='postCreate'),
    path('blog/<int:pk>/update', PostsUpdateView.as_view(), name='postUpdate'),
    path('blog/<int:pk>/delete', PostsDeleteView.as_view(), name='postDelete'),
    path('about/', views.about, name='about'),

]
