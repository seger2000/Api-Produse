from rest_framework import viewsets
from . import models
from . import serializers


class ProduseViewset(viewsets.ModelViewSet):
    queryset = models.Produse.objects.all()
    serializer_class = serializers.ProduseSerializer