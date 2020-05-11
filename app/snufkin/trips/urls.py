from django.urls import path

from . import views

app_name = "trips"
urlpatterns = [
    path("list/", views.TripsListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.TripsDetailView.as_view(), name="detail"),
    path("add/", views.TripsAddView.as_view(), name="add"),
    path("edit/<int:pk>/", views.TripsEditView.as_view(), name="edit"),
    path("delete/<int:pk>/", views.TripsDeleteView.as_view(), name="delete"),
]
