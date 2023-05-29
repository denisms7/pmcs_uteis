import pandas as pd
import numpy as np

caminho = 'contatos.csv'
df = pd.read_csv(caminho, encoding='ANSI', delimiter=";")
df = df.fillna(value='-')


# Saida:
df_contato = df.values.tolist()
df_categoria = sorted(df['secretaria'].unique())



