from django.test import TestCase

from ..factories import PlaceFactory
from snufkin.trips.factories import TripFactory


class PlaceTestCase(TestCase):
    def test_str_returns_name(self):
        place = PlaceFactory.create()
        self.assertEqual(str(place), place.name)

    def test_has_trip_returns_true_if_place_has_trips(self):
        place = PlaceFactory.create()
        TripFactory.create(places=[place])
        self.assertTrue(place.has_trip())

    def test_has_trip_returns_false_if_place_has_not_trips(self):
        place = PlaceFactory.create()
        self.assertFalse(place.has_trip())
