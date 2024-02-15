# svetofors/urls.py
from django.urls import path

from svetofors import views

app_name = "svetofors"

urlpatterns = [
    path("", views.index, name="index"),
]