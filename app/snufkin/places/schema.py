import graphene
import graphene_django

from . import models
from snufkin.trips.schema import TripType


class PlaceType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.Place

    trips = graphene.List(TripType)

    def resolve_trips(self, *args):
        return self.trips.all()


class Query(graphene.ObjectType):
    place = graphene.Field(PlaceType, id=graphene.ID())
    places = graphene.List(PlaceType)

    def resolve_places(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return models.Place.objects.none()
        return models.Place.objects.filter(user=user)

    def resolve_place(self, info, id):
        user = info.context.user
        if not user.is_authenticated:
            return models.Place.objects.none()
        return models.Place.objects.get(user=user, id=id)
