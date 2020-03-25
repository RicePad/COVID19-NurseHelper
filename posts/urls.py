from django.urls import path
from .views import PostListView, UserPosts, PostDetailView, PostCreateView
from django.conf.urls import url


app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name="all"),
    path('new', PostCreateView.as_view(), name="create" ),
    url(r'by/(?P<username>[-\w]+)/$', UserPosts.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$", PostDetailView.as_view(),name="single"),

]
