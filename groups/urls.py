from django.urls import path
from django.conf.urls import url
from .views import ListGroups, CreateGroupView, SingleGroup, JoinGroup, LeaveGroup


app_name = "groups"

urlpatterns = [
   path('', ListGroups.as_view(), name="all"),
   path('new/', CreateGroupView.as_view(), name="create"),
   path('posts/in/<int:pk>/', SingleGroup.as_view(), name="single"),
   url(r"^posts/in/(?P<slug>[-\w]+)/$", SingleGroup.as_view(),name="single"),
   url(r"join/(?P<slug>[-\w]+)/$",JoinGroup.as_view(), name="join"),
   url(r"leave/(?P<slug>[-\w]+)/$", LeaveGroup.as_view(),name="leave"),
]