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


class TripUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        start_date = graphene.Date(required=True)
        end_date = graphene.Date(required=True)
        places = graphene.List(graphene.ID)

    trip = graphene.Field(TripType)

    def mutate(self, info, id, name, description, start_date, end_date, places=[]):
        trip = models.Trip.objects.get(pk=id)
        trip.name = name
        trip.description = description
        trip.start_date = start_date
        trip.end_date = end_date
        trip.places.set(places)
        trip.save()
        return TripUpdateMutation(trip=trip)


class TripAddMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        start_date = graphene.Date(required=True)
        end_date = graphene.Date(required=True)
        places = graphene.List(graphene.ID)

    trip = graphene.Field(TripType)

    def mutate(self, info, name, description, start_date, end_date, places=[]):
        trip = models.Trip.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            user=info.context.user,
        )

        trip.places.set(places)
        trip.save()
        return TripAddMutation(trip=trip)


class Mutation(graphene.ObjectType):
    update_trip = TripUpdateMutation.Field()
    add_trip = TripAddMutation.Field()
