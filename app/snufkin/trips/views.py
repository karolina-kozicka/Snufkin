from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms


class TripsListView(LoginRequiredMixin, generic.ListView):
    template_name = "trips/list.html"
    model = models.Trip
    context_object_name = "trips"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TripsDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "trips/delete.html"
    model = models.Trip
    success_url = reverse_lazy("trips:list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TripsAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "trips/add.html"
    model = models.Trip
    form_class = forms.TripForm
    success_url = reverse_lazy("trips:list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class TripsEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = "trips/edit.html"
    model = models.Trip
    form_class = forms.TripForm
    success_url = reverse_lazy("trips:list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class TripsDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "trips/delete.html"
    model = models.Trip
    success_url = reverse_lazy("trips:list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TripsDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "trips/detail.html"
    model = models.Trip
    context_object_name = "trip"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
