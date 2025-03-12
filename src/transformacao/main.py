import pandas as pd 
import sqlite3
from datetime import datetime


#carrega o arquivo csv criado pelo crawler
df = pd.read_csv('../../data/data.csv')

#cria uma coluna com a data da coleta
df['data_coleta'] = datetime.now()

#mostrar o site de onde foram tirados os dados
df['source'] = 'https://lista.mercadolivre.com.br/tenis-corrida-masculino'

#converte os valores para float
df['old_price_reais'] = df['old_price_reais'].fillna(0)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0)
df['new_price_reais'] = df['new_price_reais'].fillna(0)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0)


df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex = True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

#configuração para mostrar todas as colunas
pd.options.display.max_columns = None

#criando uma coluna com os valores finais novos e antigos
df['old_price'] = df['old_price_reais'] + df['old_price_centavos']/100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos']/100

#remove as colunas antigas do preço
df.drop(columns = ['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], axis=1, inplace=True)


# cria a conexão com o banco de dados
conn = sqlite3.connect('../data/quotes.db')
print('Conexão com o banco de dados realizada com sucesso')

# Salva o dataframe no banco de dados
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

#fecha a conexão com o banco de daddos

conn.close()


print(df.head())



