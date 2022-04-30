from django.urls import path, include
from . import views
from app.dash_apps import vendas_carros
from app.dash_apps import vendas_ano
from app.dash_apps import vendas_veiculo
from app.dash_apps import vendas_vendedor
from app.dash_apps import comissao_vendedor
from app.dash_apps import faturamento_vendedor

import app


urlpatterns = [
    path('', views.index, name='index'),
]