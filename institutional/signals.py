from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import OfficialAddress, Category


OFFICIAL_ADDRESSES = [
    {
        "name": "Secretaria Municipal da Saúde",
        "address": "Av. Pref. Vanderlei Antunes de Morães, 644 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8044",
        "maps": "https://goo.gl/maps/VPcQBL5NH9eJBGQL6",
        "category": 2,
        
    },
    {
        "name": "Academia de Saúde",
        "address": "Rua Luiz Carlos Castoldi, s/n - Conjunto Maximino P. Santos",
        "operation": "Segunda a Sexta-feira das 08:00 as 17:00",
        "phone": "(43) 3675-8042",
        "maps": "",
        "category": 2,
    },
    {
        "name": "Hospital Municipal Dr. Lauro Marcedo Sobrinho",
        "address": "Rua Nossa Sra. do Rocio, 583 - Centro",
        "operation": "24 horas",
        "phone": "(43) 3675-8041",
        "maps": "https://goo.gl/maps/7Kep51VDMjfkMx2m7",
        "category": 2,
    },
    {
        "name": "UBS - Unidade Basica De Saúde Anita Canet",
        "address": "Avenida Wanderley Antunes Moraes, 850 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8042",
        "maps": "https://goo.gl/maps/z3bvvqJBG6v3ksGS8",
        "category": 2,
    },
    {
        "name": "UBS - Unidade Basica De Saúde Ana Garcia Ramos",
        "address": "Rua Dom Geraldo Fernandes, s/n - Conjunto Maximino P. Santos",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8042",
        "maps": "https://goo.gl/maps/TUoejjjmPC3NPCow5",
        "category": 2,
    },
    {
        "name": "UBS - Unidade Basica de Saúde Vila Progresso",
        "address": "Avenida Brasil, s/n - Vila Progresso",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8042",
        "maps": "",
        "category": 2,
    },
    {
        "name": "UAPSF - Unidade de Atendimento Primário à Saúde da Família",
        "address": "Avenida Wanderley Antunes Moraes, 1369 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8042",
        "maps": "https://goo.gl/maps/CNLqgaWcJ3vyb7t48",
        "category": 2,
    },
    {
        "name": "Paço Municipal",
        "address": "Praça Aurélio Basso, 378 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8000",
        "maps": "https://goo.gl/maps/wo6QNBRGHYg8s7DM7",
        "category": 4,
    },
    {
        "name": "Secretaria de Agricultura e Meio Ambiente",
        "address": "Rua Bruno Poleto, 31 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8000",
        "maps": "",
        "category": 8,
    },
    {
        "name": "Secretaria de Educação",
        "address": "Rua Prefeito Aparecido Ferreira Lima, 00 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8048",
        "maps": "",
        "category": 1,
    },
    {
        "name": "Secretaria de Esporte Cultura e Lazer",
        "address": "Rua Dr. Derly de Oliveira N° 721 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8000",
        "maps": "",
        "category": 3,
    },
    {
        "name": "Secretaria de Assistência Social",
        "address": "Rua Desembargador Munhoz de Melo, 385 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8035",
        "maps": "",
        "category": 7,
    },
    {
        "name": "CREAS - Centro de Referência Especializado de Assistência Social",
        "address": "Rua Sulaiman Felicio , 651 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8035",
        "maps": "",
        "category": 7,
    },
    {
        "name": "CRAS - Centro de Referência de Assistência Social",
        "address": "Rua Dezembargador Munhoz de Melo, 746 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8035",
        "maps": "",
        "category": 7,
    },
    {
        "name": "Conselho Tutelar",
        "address": "Rua João Alves da Silva Neto, 77 - Conjunto Adalgiza B. Felício",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8038",
        "maps": "",
        "category": 7,
    },
    {
        "name": "Secretaria de Infra Estrutura e Serviços Publicos",
        "address": "Rua Engenheiro Wilson Daminhao, s/n - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8030",
        "maps": "",
        "category": 5,
    },
    {
        "name": "Patio (Antigo DR)",
        "address": "Wilson Daminhão, 891 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 17:00",
        "phone": "(43) 3675-8030",
        "maps": "",
        "category": 5,
    },
    {
        "name": "Terminal Rodoviário de Centenário do Sul",
        "address": "Rua Nossa Sra. do Rocio, s/n - Centro",
        "operation": "Segunda a Sexta-feira das 06:00 as 22:00",
        "phone": "(43) 3675-8005",
        "maps": "",
        "category": 4,
    },
    {
        "name": "Cozinha Comunitária de Centenário do Sul",
        "address": "xxxxxxxx - Centro",
        "operation": "Segunda a Segunda das 06:00 as 22:00",
        "phone": "",
        "maps": "",
        "category": 7,
    },
    {
        "name": "Cozinha Central",
        "address": "xxxxxxxx - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8049",
        "maps": "",
        "category": 1,
    },
    {
        "name": "Biblioteca Cidadã Professora Maria Aparecida de Lima Dias",
        "address": "Rua Maziad Felício, 30 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 11:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8000",
        "maps": "",
        "category": 3,
    },
    {
        "name": "Escola Municipal Irmã Osmunda – Ensino Fundamental I",
        "address": "Rua Francisco Brigido Dutra, 714 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 12:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8045",
        "maps": "",
        "category": 1,
    },
    {
        "name": "Escola Municipal José De Anchieta – Ensino Fundamental I",
        "address": "Rua Vereador Antonio Pereira da Silva, 820 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 12:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8045",
        "maps": "",
        "category": 1,
    },
    {
        "name": "Escola Municipal São José – Ensino Fundamental I",
        "address": "Rua João Severiano Ferreira, 105 - Conjunto Habitacional Adalgiza Aparecida Bueno Felício",
        "operation": "Segunda a Sexta-feira das 08:00 as 12:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8045",
        "maps": "",
        "category": 1,
    },
    {
        "name": "Escola Municipal Prefeito Afonso Belenda – Ensino Fundamental I",
        "address": "Rodovia Fuad Nacli, Km 01 - Vila Progresso",
        "operation": "Segunda a Sexta-feira das 08:00 as 12:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8045",
        "maps": "",
        "category": 1,
    },
    {
        "name": "Centro Municipal de Educação Ulysses Pessoa de Lima",
        "address": "Rua Generino Fernandes Leão, 188 - Parque Industrial José Augusto Ferreira",
        "operation": "Segunda a Sexta-feira das 08:00 as 12:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8045",
        "maps": "",
        "category": 1,
    },
    {
        "name": "CEI - Centro De Educação Infantil Menino Jesus I",
        "address": "Rua Vereador Maziad Felício, nº 615 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 12:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8045",
        "maps": "",
        "category": 1,
    },
    {
        "name": "CEI - Centro De Educação Infantil Menino Jesus III",
        "address": "Rua João Alves da Silva Neto, 127 - Conjunto Habitacional Adalgiza Aparecida Bueno Felício",
        "operation": "Segunda a Sexta-feira das 08:00 as 12:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8045",
        "maps": "",
        "category": 1,
    },
    {
        "name": "CEI - Centro de Educação Infantil Menino Jesus V",
        "address": "Avenida Brasil, s/n - Vila Progresso",
        "operation": "Segunda a Sexta-feira das 08:00 as 12:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8045",
        "maps": "",
        "category": 1,
    },
    {
        "name": "Ginásio de Esportes José Ferreira Lima",
        "address": "Rua Derly de Oliveira, s/n - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 12:00 e das 13:00 as 17:00",
        "phone": "(43) 3675-8000",
        "maps": "",
        "category": 3,
    },
    {
        "name": "Estadio Muncipal Sérgio Vito Meca",
        "address": "Av. Pref. Wanderley A. de Moraes, 243 - Centro",
        "operation": "Segunda a Sexta-feira das 08:00 as 17:00",
        "phone": "s/n",
        "maps": "",
        "category": 3,
    },
    {
        "name": "Teatro Muncipal",
        "address": "Rua Prefeito Aparecido Ferreira Lima, s/n - Centro",
        "operation": "Agendamento",
        "phone": "(43) 3675-8000",
        "maps": "",
        "category": 3,
    },
]


@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    """
    Cria categorias padrão com IDs fixos (1 a 5) após a migração.
    """
    default_categories = {
        1: "Educação",
        2: "Saúde",
        3: "Cultura",
        4: "Administração",
        5: "Infraestrutura",
        6: "Segurança",
        7: "Assistência Social",
        8: "Meio Ambiente",
        9: "Transporte",
        10: "Habitação",
        11: "Esporte e Lazer",
        12: "Turismo",
    }

    for pk, name in default_categories.items():
        Category.objects.update_or_create(
            id=pk,
            defaults={"name": name},
        )


@receiver(post_migrate)
def create_official_addresses(sender, **kwargs):
    if sender.name != "institutional":
        return

    for data in OFFICIAL_ADDRESSES:
        try:
            category = Category.objects.get(pk=data["category"])
        except Category.DoesNotExist:
            print('ERRO')
            continue  # ou levante erro, se quiser obrigar a existir

        OfficialAddress.objects.get_or_create(
            name=data["name"],
            defaults={
                "address": data.get("address", ""),
                "operation": data.get("operation", ""),
                "phone": data.get("phone", ""),
                "maps": data.get("maps", ""),
                "category": category,
            },
        )
