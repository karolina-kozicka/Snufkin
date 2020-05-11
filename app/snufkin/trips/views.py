from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class TripsListView(LoginRequiredMixin, generic.ListView):
    template_name = "trips/list.html"
    model = models.Trip
    context_object_name = "trips"


class TripsDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "trips/delete.html"
    model = models.Trip
    success_url = reverse_lazy("trips:list")


class TripsAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "trips/add.html"
    model = models.Trip
    fields = ("name", "description", "start_date", "end_date", "places")
    # TODO form_class
    success_url = reverse_lazy("trips:list")


class TripsEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = "trips/edit.html"
    model = models.Trip
    fields = ("name", "description", "start_date", "end_date", "places")
    success_url = reverse_lazy("trips:list")


class TripsDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "trips/delete.html"
    model = models.Trip
    success_url = reverse_lazy("trips:list")


class TripsDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "trips/detail.html"
    model = models.Trip
    context_object_name = "trip"

