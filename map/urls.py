from django.urls import path
from .views import StopsView, RoutesView

urlpatterns = [
    path("stops/", StopsView.as_view(), name="Stop-list"),
    path("routes/<int:bus_number>/", RoutesView.as_view(), name="Route-list"),
]
