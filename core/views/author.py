from rest_framework.viewsets import ModelViewSet

from core.models import Author
from core.serializers import AuthorSerializer

import json

from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def getAuthors(request):
        authors = list((Author.objects.all()).values())
        return JsonResponse(authors, content_type="text/json-comment-filtered", safe=False)

    def addAuthor(request):
        body = json.loads(request.body.decode('utf-8'))

        author = Author.objects.create(
            name_author = body["name_author"],
            author_biography = body["author_biography"]
        )

        author.save()

        return HttpResponse("Autor criado com sucesso!")