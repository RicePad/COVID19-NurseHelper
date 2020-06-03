import graphene
import posts.queries


class Query(posts.queries.QueryType, graphene.ObjectType):
    pass




schema = graphene.Schema(query=Query)
