from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("faq", views.faq, name="faq"),
    path("catalog", views.catalog, name="catalog"),
    path("cards_catalog", views.cards_catalog, name="cards_catalog")
]
