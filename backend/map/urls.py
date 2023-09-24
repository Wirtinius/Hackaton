from django.urls import path
from .views import StopsView, RoutesView, BusesView

urlpatterns = [
    path("stops/", StopsView.as_view(), name="Stop-list"),
    path("routes/<int:bus_number>/", RoutesView.as_view(), name="Route-list"),
    path("buses/", BusesView.as_view(), name="Bus-list"),
    path("buses/<int:bus_number>/", BusesView.as_view(), name="Bus-list"),
]
