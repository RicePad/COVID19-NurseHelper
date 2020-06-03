import graphene
from graphene_django import DjangoObjectType
from .models import Post
from .schema import PostType


class QueryType(graphene.ObjectType):
    posts = graphene.List(PostType)

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()
