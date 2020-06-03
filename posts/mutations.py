import graphene
from graphene_django import DjangoObjectType
from .models import Post
from .schema import PostType

class CreatePost(graphene.Mutation):
    user = graphene.String()
    message = graphene.String()

    #2
    class Arguments:
        user = graphene.String()
        message = graphene.String()

    #3
    def mutate(self, info, url, description):
        post = Post(user=user, message=message)
        post.save()

        return CreatePost(
            id=user.id,
            user=post.user,
            message=post.description,
        )