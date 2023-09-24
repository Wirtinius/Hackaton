from django.urls import path

from .views import GenerateView, video


urlpatterns = [
    path("generate/", GenerateView.as_view(), name="generate"),
    path("video/", video )
]