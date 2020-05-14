import graphene

import posts.schema


class Query(posts.schema.QueryType, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
