# Bibliotecas para analise
import pandas as pd

# Bibliotecas para gráficos
from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc

# Cria o APP
app = DjangoDash(
    'vendas_ano',
    # assets_external_path='<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'
    
)

# Carrregando a base de dados 
Base_Dados = pd.read_excel("Vendas.xlsx")

# Soma as vendas por dia
Vendas_Dias = Base_Dados.groupby(pd.Grouper(key='DataVenda', axis=0, freq='D')).sum().reset_index()

# Capturando o nome dos veiculos
Nome_Veiculo = Base_Dados['Veiculo'].value_counts()

app.layout = html.Div(
    children = [
        # Gráfico de Linhas - Vendas por período
        # ------------------------------------------------
        dcc.Graph(
            id='vendasPeriodo',
            figure = { 
                'data': [
                    {
                        'x': Vendas_Dias['DataVenda'], 
                        'y': Vendas_Dias['ValorVenda'], 
                        'type': 'line', 
                        'name': 'Total de Vendas (mil)'
                    },
                ],
                'layout': {
                    'title': 'Total de Vendas entre Outubro e Dezembro (mil)',
                    'xaxis': {'title': 'Período'},
                    'yaxis': dict(title= 'Valor'),
                    'titlefont': {'size': 22, 'z': 8},     
                    'height': 240,   
                }
            }
        ), 
        # ------------------------------------------------
    ], 
)