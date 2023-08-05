#importa feramentas: pandas numpy e plotly
import pandas as pd
import numpy
import plotly.express as px # serve para visualizar os dados em gráficos
#visualizar base de dados
tab=pd.read_csv("cancelamentos.csv")
can=tab[["cancelou"]].value_counts() # para saber o tanto de cancelamento que tem, é cerca de 50%
print(can)
#mostrar  um resumo de informações da base de dados
print(tab.info())# me mostrou que tenho parte do meu banco de dados que esta vazio
tab=tab.dropna()# Tira os valores em branco da base
print(tab.info())# Para visualizar se os dados em branco foram retirados
# Tirar a coluna CustomerID  pois para a análise não faz sentido que ela permaneça
tab=tab.drop("CustomerID", axis=1)
""" da tabela vou tirar a coluna "axis=1" e o nome da coluna, obs"axis=0 é para linhas e axis=1 coluna"
juntar as informações para conseguir entender os cancelamentos, vou usar o plotly para ver algumas informações em gráficos
sempre relacionando cancelamento com uma das outras informações da base.
esse gráficos serão abertos em uma página na web"""

for coluna in tab.columns:              # laço de repetição para criar os gráficos
    grafico= px.histogram(tab, x=coluna, color="cancelou")
    grafico.show()
"""com os graficos é possivel concluir que melhorando alguns cenários, como exemplo não ofertando mais o plano
 mensal, o cancelamento ira reduzir, segue abaixo  alguns tratamentos"""


tab=tab[tab["idade"]<=51]
tab=tab[tab["sexo"]!="Male"]
tab=tab[tab["ligacoes_callcenter"]<=4]
tab=tab[tab["dias_atraso"]<=19]
tab=tab[tab["assinatura"]=="Standard"]
tab=tab[tab["duracao_contrato"]!="Monthly"]
tab=tab[tab["total_gasto"]>=500]
print(tab)
print(tab["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
"""com esse tratamento o cancelamento reduziu  para cancelou
0.0    90.3%
1.0     9.7%"""