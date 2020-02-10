"""apicenipa2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import  include
from django.urls import path
from rest_framework import routers
from aeronaves.views import ArenovaesViewsets
from fator.views import FatorViewset
from ocorrencias.views import OcorrenciaViewSet
from recomendacaoSeg.views import RecomendacaoSegViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Api Cenipa 2020",
      default_version='v1',
      description="Dados estruturados de acidentes e incidentes aŕeos via Cenipa ",
      #terms_of_service="https://www.google.com/policies/terms/",
      #contact=openapi.Contact(email="contact@snippets.local"),
      #license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'aeronaves', ArenovaesViewsets)
router.register(r'fator', FatorViewset)
router.register(r'ocorrencias', OcorrenciaViewSet)
router.register(r'recomendacaoSeg', RecomendacaoSegViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),
]
