from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Ocorrencias
from .serializers import OcorrenciaSerializers
from django_filters.rest_framework import DjangoFilterBackend

class OcorrenciaViewSet(ModelViewSet):
    queryset = Ocorrencias.objects.all()
    serializer_class = OcorrenciaSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['codigo_ocorrencia']