"""
URL configuration for example_project project.
"""

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
]
