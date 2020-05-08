from django.urls import path

from . import views

app_name = 'places'
urlpatterns = [
    path('list/', views.PlacesListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.PlacesDetailView.as_view(), name='detail'),
    path('add/', views.PlacesAddView.as_view(), name='add'),
    path('edit/<int:pk>/', views.PlacesEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.PlacesDeleteView.as_view(), name='delete'),
]