# Bibliotecas para analise
import pandas as pd

# Bibliotecas para gráficos
from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc

# Cria o APP
app = DjangoDash(
    'comissao_vendedor',
    # assets_external_path='<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'
    
)

# Carrregando a base de dados 
Base_Dados = pd.read_excel("Vendas.xlsx")

# Somatória por Vendedor
Vendedor_Comissao = Base_Dados.groupby(['Vendedor']).sum()

# HTML
app.layout = html.Div(
    children = [
        dcc.Graph(
            id='comissaoVendedor',
            figure = { 
                'data': [
                    {
                        'x': Vendedor_Comissao.index,
                        'y': Vendedor_Comissao['Comissao'],
                        'type': 'bar', 
                    },
                ],
                'layout': {
                    'title': 'Comissão por Vendedor (mil)',
                    'color': '#00CC99',
                    'xaxis': {'title': 'Vendedor'},
                    'yaxis': dict(title= 'Valor Comissão (mil)'),
                    'titlefont': {'size': 22, 'z': 8},
                    'height': 300
                }
            }
        ),
    ]
)