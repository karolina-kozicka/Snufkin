from django.shortcuts import render
from django.views import generic

from . import models


class TripsListView(generic.ListView):
    template_name = "trips/list.html"
    model = models.Trip
    context_object_name = 'trips'