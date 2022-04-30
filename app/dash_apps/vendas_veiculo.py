# Bibliotecas para analise
import pandas as pd
import numpy as np

# Bibliotecas para gráficos
from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc

# Cria o APP
app = DjangoDash(
    'vendas_veiculo',
    # assets_external_path='<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'
    
)

# Carrregando a base de dados 
Base_Dados = pd.read_excel("Vendas.xlsx")

# Capturando o nome dos veiculos
Nome_Veiculo = Base_Dados['Veiculo'].value_counts()

# HTML
app.layout = html.Div(
    children = [
        # Gráfico de Barras - Vendas por veiculo
        # ------------------------------------------------
        dcc.Graph(
            id='vendasVeiculo',
            figure = { 
               'data': [
                   {
                       'y': Base_Dados['Veiculo'].value_counts(), 
                       'x': Nome_Veiculo[:5].index, 
                       'type': 'bar', 
                       'name': 'Total de Vendas dos 5 mais vendidos (mil)'
                   },
               ],
               'layout': {
                   'title': 'Total dos 5 veiculos mais vendidos (und)',
                   'xaxis': {'title': 'Veículo'},
                   'yaxis': dict(title= 'Quantidade Vendida'),
                   'titlefont': {'size': 22, 'z': 8},
                   'height': 240,
               }
            }
        )
        # ------------------------------------------------
    ]
)
