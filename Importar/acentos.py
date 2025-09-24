import os
from unidecode import unidecode
import chardet

caminho_arquivo = r'C:\Projetos\pmcs_uteis-2.0\numros_ok.csv'

if not os.path.isfile(caminho_arquivo):
    print("Arquivo não encontrado!")
    exit()

# Detecta a codificação do arquivo
with open(caminho_arquivo, 'rb') as f:
    rawdata = f.read()
    resultado = chardet.detect(rawdata)
    encoding = resultado['encoding']

# Lê o conteúdo com a codificação detectada
with open(caminho_arquivo, 'r', encoding=encoding) as f:
    conteudo = f.read()

# Remove acentos e cedilha
conteudo_sem_acentos = unidecode(conteudo)

# Salva o arquivo alterado
with open(caminho_arquivo, 'w', encoding='utf-8') as f:
    f.write(conteudo_sem_acentos)

print("Acentos e cedilha removidos com sucesso!")
