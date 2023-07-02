import pandas as pd
import requests

class BCB_api:
    def __init__(self, qnt_data=10000):
        self.qnt_data = qnt_data
        self.skip_index = 0
        self.count = 0
        self.df_init = pd.DataFrame()

    def make_request(self):
        while True:
            for i in range(1):
                self.count += 1

            print(f'Capturando tabela {self.count}')
            url = f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top={self.qnt_data}&$skip={self.skip_index}&$orderby=Data%20desc&$format=json'
            req = requests.get(url)
            data = req.json()

            df = pd.DataFrame(data['value'])

            if len(data['value']) < 1:
                break

            df['Valor'] = df['Valor'].map('R${:,.2f}'.format)
            df['Quantidade'] = df['Quantidade'].map('{:,.3f}'.format)

            self.df_init = pd.concat([self.df_init, df])
            self.skip_index += self.qnt_data

    def export_to_excel(self, filename):
        print(self.df_init)
        print('Criando arquivo excel...')
        self.df_init.to_excel(filename, index=False)

    def export_to_parquet(self, filename):
        print('Criando arquivo parquet...')
        self.df_init.to_parquet(filename)

    def run(self):
        self.make_request()
        self.export_to_excel('BCB_circulacao.xlsx')
        self.export_to_parquet('BCB_circulacao.parquet')
        print('FINISH')

if __name__ == '__main__':
    req = BCB_api()
    req.run()
