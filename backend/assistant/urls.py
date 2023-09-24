from django.urls import path

from .views import GenerateView


urlpatterns = [
    path("generate/", GenerateView.as_view(), name="generate"),
]