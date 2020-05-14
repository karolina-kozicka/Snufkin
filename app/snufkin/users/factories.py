import factory

from . import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    name = factory.Sequence(lambda n: "User {n}")
    email = factory.Sequence(lambda n: "user{n}@example.com")

