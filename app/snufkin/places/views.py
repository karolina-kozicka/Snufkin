from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class PlacesListView(LoginRequiredMixin, generic.ListView):
    template_name = "places/list.html"
    model = models.Place
    context_object_name = "places"


class PlacesDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "places/detail.html"
    model = models.Place
    context_object_name = "place"


class PlacesAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "places/add.html"
    model = models.Place
    fields = (
        "name",
        "point",
    )
    # TODO form_class
    success_url = reverse_lazy("places:list")


class PlacesEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = "places/edit.html"
    model = models.Place
    fields = (
        "name",
        "point",
    )
    success_url = reverse_lazy("places:list")


class PlacesDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "places/delete.html"
    model = models.Place
    success_url = reverse_lazy("places:list")

