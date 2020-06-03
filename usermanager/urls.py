
from django.contrib import admin
from django.urls import path, include
from classroom.views import NurseSignUpView, HelperSignUpView
from .views import HomeView
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', HomeView.as_view(), name="home"),
    path('accounts/signup/nurse/', NurseSignUpView.as_view(), name='nurse_signup'),
    path('accounts/signup/helper/', HelperSignUpView.as_view(), name='helper_signup'),
    path('groups/', include('groups.urls', namespace="groups")),
    path('posts/', include('posts.urls', namespace="posts")),
]
