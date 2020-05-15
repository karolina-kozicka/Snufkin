from django.test import TestCase

from ..factories import TripFactory


class TripsTestCase(TestCase):
    def test_str_returns_name(self):
        trip = TripFactory.create()
        self.assertEqual(str(trip), trip.name)

    def test_duration_returns_difference_between_end_and_start_dates(self):
        trip = TripFactory.create()
        self.assertEqual(trip.duration(), trip.end_date - trip.start_date)

