import graphene
from workshop.schema import Query
from workshop.views import Carshop 

# from workshop.views import Mutation as workshop_mutation
# from workshop.schema import Query as workshop_query


class Query(Query,graphene.ObjectType):
    pass


class Mutation(Carshop,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)