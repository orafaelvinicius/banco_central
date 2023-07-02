from pprint import pprint
import requests
import pandas as pd
import numpy as np
import json



# class BCB_Cedulas:
#     def __init__(self, url):
#         self.url
#         self.data

#     def request(url):        
#         req = requests.get(url)
#         data = req.json()
#         #pprint(data)
#         return data

    

#     def create_df(data):
#         df = pd.DataFrame(data)

#         # #Formatação de valores
#         # df['Valor'] = df['Valor'].map('R${:,.2f}'.format)

#         return df
    
#     def pagination(self, url, data):
#         df_init = pd.DataFrame()

#         while True:
#             self.request(url)
#             table = self.create_df(data)
#             if len(data['value']) < 1:
#                 break
#             df_init = pd.concat([df_init], table )

#     # def main(self, url):
#     #     return self.request(url)


# # url = 'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=1000&$orderby=Data%20desc&$format=json'
# url = f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top={qnt_data}&$skip={skip_index}&$orderby=Data%20desc&$format=json'
# data = BCB_Cedulas.request(url)
# df = BCB_Cedulas.create_df(data['value'])
# print(df)


def req_pagination():

    
    df_init = pd.DataFrame()
    skip_index = 0
    qnt_data = 10000
    count = 0


    while True:
        for i in range(10):
            count += 1
        
        print(f'Capturando tabela {count}')
        url = f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top={qnt_data}&$skip={skip_index}&$orderby=Data%20desc&$format=json'
        req = requests.get(url)
        data = req.json()

        df = pd.DataFrame(data['value'])

        if len(data['value']) < 1:
            break
        df_init = pd.concat([df_init, df])
        skip_index += qnt_data

    print(df_init)
    print('Criando arquivo excel...')

    df_init.to_excel('BCB_circulacao.xlsx', index=False)

    '''
    Dica++: Exportei os dados também no formato parquet 
        por se tratar do formato ideal para a transação de dados
        entre sistemas por ser mais leve 
    '''

    print('Criando arquivo parquet...')
    df_init.to_parquet('BCB_circulacao.parquet')
    
    print('FINISH')

req_pagination()
