from django.urls import path

from . import views

app_name = 'trips'
urlpatterns = [
    path('list/', views.TripsListView.as_view(), name='list'),
]