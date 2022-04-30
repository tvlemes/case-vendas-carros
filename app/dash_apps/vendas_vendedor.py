# Bibliotecas para analise
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Bibliotecas para gráficos
from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc


# Cria o APP
app = DjangoDash(
    'vendas_vendedor',
    # assets_external_path='<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'
    
)

# Carrregando a base de dados 
Base_Dados = pd.read_excel("Vendas.xlsx")

# Top 3 Vendedores
Vendedor = Base_Dados['Vendedor'].value_counts(normalize=True)*100
Top3 = Vendedor[:3]
Outros = pd.Series(Vendedor[-3:].sum(), index=['Outros']) # Criando uma serie
Vendas_Vendedor = pd.Series(Top3.append(Outros, # Mesclando Series
                  ignore_index = False))
labels='José Antônio', 'Maria Aparecida', 'Pedro Hertz', 'Outros' 
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(Vendas_Vendedor)))

# HTML
app.layout = html.Div(
    children = [
        html.Div(id='vendedor',
            children=[

                # Gráfico de Pizza - Top 3 Vendedores
                # ------------------------------------------------
                dcc.Graph(
                    id='vendasVendedor',
                    figure = { 
                        'data': [
                            {
                                'values': Vendas_Vendedor, 
                                'labels': labels,
                                'type': 'pie', 
                            },
                        ],
                        'layout': {
                            'title': 'Vendas por Vendedores - Top 3',
                            'colors': colors,
                            'titlefont': {'size': 22, 'z': 8},
                            'height': 300
                        }
                    }
                ),
            ]           

        )
    ]
)