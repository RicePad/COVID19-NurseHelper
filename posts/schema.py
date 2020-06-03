import graphene
from graphene_django import DjangoObjectType

from .models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post

        
