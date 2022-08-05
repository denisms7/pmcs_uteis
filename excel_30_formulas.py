import os


pasta = './static/videos/excel_30_formulas'
dados_video = []

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        dados_video.append({'caminho': f'{diretorio[8:]}/{arquivo}', 'arquivo': arquivo})




