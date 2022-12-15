from rest_framework.viewsets import ModelViewSet

from core.models import Genre
from core.serializers import GenreSerializer

from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse
from django.http import JsonResponse
import json


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def getGenres(request):
        genres = list((Genre.objects.all()).values())
        return JsonResponse(genres, content_type="text/json-comment-filtered", safe=False)
    
    def addGenre(request):
        body = json.loads(request.body.decode('utf-8'))

        genre = Genre.objects.create(
            name_genre = body["name_genre"],
            description = body["description"]
        )

        genre.save()

        return HttpResponse("Gênero criado com sucesso!")