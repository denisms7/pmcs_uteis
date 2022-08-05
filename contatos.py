import pandas as pd


caminho = 'C:\contatos PMCS\contatos.csv'
# df2 = pd.read_csv(caminho, delimiter=",")


df = [
#('numero',	'setor',	'secretaria'),
('(43) 3675-8000',	'PABX',	'boot'),
('(43) 3675-8001',	'Recepção',	'Administração'),
('(43) 3675-8002',	'RH',	'Administração'),
('(43) 3675-8003',	'off-line',	'boot'),
('(43) 3675-8004',	'Tributacao',	'Fazenda'),
('(43) 3675-8005',	'Contabilidade',	'Fazenda'),
('(43) 3675-8006',	'off-line',	'boot'),
('(43) 3675-8007',	'Contabilidade',	'Fazenda'),
('(43) 3675-8008',	'Tesouraria',	'Fazenda'),
('(43) 3675-8009',	'Compras',	'Fazenda'),
('(43) 3675-8010',	'Ouvidoria',	'Gabinete'),
('(43) 3675-8011',	'off-line',	'boot'),
('(43) 3675-8012',	'Assesoria Juridica',	'Administração'),
('(43) 3675-8013',	'Licitação',	'Administração'),
('(43) 3675-8014',	'Chefe de Gabinete',	'Gabinete'),
('(43) 3675-8015',	'Administração',	'Administração'),
('(43) 3675-8016',	'Informatica',	'Administração'),
('(43) 3675-8017',	'off-line',	'boot'),
('(43) 3675-8018',	'Gabinete',	'Gabinete'),
('(43) 3675-8019',	'Controladoria (Daiane)',	'Controle Interno'),
('(43) 3675-8020',	'Secretaria de Gabinete',	'Gabinete'),
('(43) 3675-8021',	'off-line',	'boot'),
('(43) 3675-8022',	'Administração (Fernando)',	'Administração'),
('(43) 3675-8023',	'Juridico',	'Administração'),
('(43) 3675-8024',	'off-line',	'boot'),
('(43) 3675-8025',	'Controladoria',	'Controle Interno'),
('(43) 3675-8027',	'off-line',	'boot'),
('(43) 3675-8026',	'Patrimonio',	'Fazenda'),
('(43) 3675-8028',	'Vice-Prefeito',	'Gabinete'),
('(43) 3675-8029',	'Industria e comercio',	'Desenvolvimento Economico'),
('(43) 3675-8030',	'Engenharia',	'Infra Estrutura')
]


df1 = pd.DataFrame(df, columns = ['Telefone', 'Sala', 'Setor'])


categoria = sorted(df1['Setor'].unique())


# categoria.sort_values(ascending=True)


# numero ; setor ; secretaria

