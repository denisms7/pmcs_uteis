import pandas as pd

caminho = 'contatos.csv'
df = pd.read_csv(caminho, encoding='ANSI', delimiter=";")

# Saida:

df_contato = list(df.itertuples(index=False))
categoria = sorted(df['setor'].unique())


