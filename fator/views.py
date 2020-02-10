from rest_framework.viewsets import ModelViewSet
from .models import Fator
from .serializers import FatorSerializers
from django_filters.rest_framework import DjangoFilterBackend

class FatorViewset(ModelViewSet):
    queryset = Fator.objects.all()
    serializer_class = FatorSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fator_nome']


