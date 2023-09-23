from django.urls import path
from .views import StopsView

urlpatterns = [
    path("stops/<int:route_id>", StopsView.as_view(), name="Stop-list"),
]
