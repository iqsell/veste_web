from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("polls.urls")),
    path("faq", include('polls.urls')),
    path("catalog", include('polls.urls')),
    path("cards_catalog", include('polls.urls')),
    path("admin/", admin.site.urls),
]
