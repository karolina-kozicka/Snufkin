import datetime
from django.test import TestCase

from ..factories import UserFactory
from snufkin.trips.factories import TripFactory


class UserTestCase(TestCase):
    def test_str_returns_email(self):
        user = UserFactory.create()
        self.assertEqual(str(user), user.email)

    def test_last_trip_returns_none_if_user_has_not_trips(self):
        user = UserFactory.create()
        self.assertIsNone(user.last_trip())

    def test_last_trip_returns_last_trip_if_user_has_trips(self):
        user = UserFactory.create()
        TripFactory.create(user=user, start_date=datetime.date(2018, 1, 1))
        trip = TripFactory.create(user=user, start_date=datetime.date(2020, 1, 1))
        TripFactory.create(user=user, start_date=datetime.date(2019, 1, 1))

        self.assertEqual(user.last_trip(), trip)
