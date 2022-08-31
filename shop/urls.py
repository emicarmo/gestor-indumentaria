from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("contacto", views.contacto, name="contacto"),
    path("nueva_remera", views.nueva_remera, name="nueva_remera"),
    path("modificar_indumentaria/<int:pk>", views.modificar_indumentaria, name="modificar_indumentaria"),
    path("eliminar_indumentaria/<int:pk>", views.eliminar_indumentaria, name="eliminar_indumentaria")
]
