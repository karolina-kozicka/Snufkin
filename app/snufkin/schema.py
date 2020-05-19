import graphene
from graphene_django.debug import DjangoDebug

from . import graphene_types
from snufkin.places import schema as places_schema
from snufkin.trips import schema as trips_schema
from snufkin.users import schema as users_schema


class Query(places_schema.Query, trips_schema.Query, users_schema.Query):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(trips_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

