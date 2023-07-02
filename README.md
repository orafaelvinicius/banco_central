# Desafio técnico para desenvolver habilidades com engenharia de dados e integações

Este desafio foi idealizado por Vitor Lindbergh como forma de incentivo para meus estudos sobre dados.

Obrigado Vitinho! s2

## Sobre o desafio:

O desafio consiste em criar um código Python que faz a extração de dados de alguma API de sua
escolha, trata e padronizar os dados que precisam ser tratados (formatos de data, números
ou valores financeiros, por exemplo) e exportam estes dados para uma planilha em Excel.

### Como foi feito:

A api escolhida foi a do banco central, esta api fornece diversos dados públicos sobre nossa moeda (R$). Os dados escolhidos para o desafio foram os de moedas em circulação que apresenta informações diárias das quantidades de cédulas e moedas em circulação (não estão incluídas as moedas comemorativas). As informações estão separadas para cada espécie (cédula ou moeda) e denominação do Real.

O código tem o objetivo de raspar todas as informações disponibilizadas pela api fazendo a coleta de 10000 linhas por requisição, passando pela formatação de dados que são inseridos e concatenados em um dataframe, que posteriormente é exportado para 2 formatos distintos de arquivos.

### Ferramentas

As ferramentas utilizadas para realizar a tarefa foram:

    * Python 3.X
    * Pandas
    * openxlm
    * requests
    * pyarrow

## Como utilizar:

    (no linux/Ubuntu)
    1. Crie um ambiente virtual `python3 -M venv venv`;
    2. Execute seu ambiente virtual `source venv/bin/activate`
    2. Instale as dependencias `pip install -r requirements.txt`;
    3. Execute o arquivo `python3 main.py`
