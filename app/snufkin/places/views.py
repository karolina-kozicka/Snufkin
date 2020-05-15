from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms


class PlacesListView(LoginRequiredMixin, generic.ListView):
    template_name = "places/list.html"
    model = models.Place
    context_object_name = "places"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class PlacesDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "places/detail.html"
    model = models.Place
    context_object_name = "place"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class PlacesAddView(LoginRequiredMixin, generic.CreateView):
    template_name = "places/add.html"
    model = models.Place
    form_class = forms.PlaceForm
    success_url = reverse_lazy("places:list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class PlacesEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = "places/edit.html"
    model = models.Place
    form_class = forms.PlaceForm
    success_url = reverse_lazy("places:list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class PlacesDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "places/delete.html"
    model = models.Place
    success_url = reverse_lazy("places:list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

