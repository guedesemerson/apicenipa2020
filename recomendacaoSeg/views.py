from rest_framework.viewsets import ModelViewSet
from .models import RecomendacaoSeg
from .serializers import RecomendacaoSegSerializers
from django_filters.rest_framework import DjangoFilterBackend

class RecomendacaoSegViewSet(ModelViewSet):
    queryset = RecomendacaoSeg.objects.all()
    serializer_class = RecomendacaoSegSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['recomendacao_numero']