from django.shortcuts import render

from music_app.models import Artist


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, "music_app/artist_list.html", {"artists": artists})
