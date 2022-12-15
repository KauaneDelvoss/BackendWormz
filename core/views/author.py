from rest_framework.viewsets import ModelViewSet

from core.models import Author
from core.serializers import AuthorSerializer

from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def getAuthors(request):
        authors = list((Author.objects.all()).values())
        return JsonResponse(authors, content_type="text/json-comment-filtered", safe=False)