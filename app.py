import pandas as pd
import requests

table_final = pd.DataFrame()
skip_index = 0
while True:
  link = f"https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={skip_index}&$orderby=Data%20desc&$format=json"
  requisicao = requests.get(link)
  informacoes = requisicao.json()
  tabela = pd.DataFrame(informacoes["value"])
  if len(informacoes['value']) < 1:
    break
  table_final = pd.concat([table_final, tabela])
  skip_index += 10000
table_final.to_excel('Dados_banco_central.xlsx', index=False)