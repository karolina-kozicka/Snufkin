import graphene
import graphene_django

from . import models


class TripType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.Trip


class Query(graphene.ObjectType):
    trip = graphene.Field(TripType, id=graphene.ID())
    trips = graphene.List(TripType)

    def resolve_trip(self, info, id):
        user = info.context.user
        if not user.is_authenticated:
            return models.Trip.objects.none()
        return models.Trip.objects.get(user=user, id=id)

    def resolve_trips(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return models.Trip.objects.none()
        return models.Trip.objects.filter(user=user)
