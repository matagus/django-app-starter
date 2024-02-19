# generate url patterns for the app
from django.urls import path

from music_app.views import artist_list


app_name = "music_app"

urlpatterns = [
    path("", artist_list, name="artist_list"),
]
