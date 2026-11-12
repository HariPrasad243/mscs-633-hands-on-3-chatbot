"""URL configuration for the qa_chatbot project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("chat.urls")),
]
