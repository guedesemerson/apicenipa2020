from rest_framework.viewsets import ModelViewSet
from .serializers import AreonavesSerializers
from .models import Aeronaves
from django_filters.rest_framework import DjangoFilterBackend

class ArenovaesViewsets(ModelViewSet):
    queryset = Aeronaves.objects.all()
    serializer_class = AreonavesSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['aeronave_matricula']
