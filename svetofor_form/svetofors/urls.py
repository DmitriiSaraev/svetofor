# svetofors/urls.py
from django.urls import path

from svetofors import views

app_name = "svetofors"

urlpatterns = [
    path("", views.index, name="index"),
    path("empty_model/", views.empty_model, name="empty_model"),
    path('svetofor/<int:svetofor_id>/up_svetofor/', views.up_svetofor, name='up_svetofor',),
    path('', views.up_svetofor_empty, name='up_svetofor_empty',),
]


