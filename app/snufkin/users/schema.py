import graphene
import graphene_django

from . import models
from snufkin.trips.schema import TripType
from snufkin.places.schema import PlaceType


class UserType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.User

    trips = graphene.List(TripType)
    places = graphene.List(PlaceType)

    def resolve_trips(self, *args):
        return self.trips.all()

    def resolve_places(self, *args):
        return self.places.all()


class Query(graphene.ObjectType):
    user = graphene.Field(UserType)

    def resolve_user(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return models.User.objects.none()
        return user
