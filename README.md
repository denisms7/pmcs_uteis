# PMCS Uteis 2.0
## 🚀 Pagina Web de atalhos e Informação 

Pagina web para auxilio dos servidores públicos do município de [Centenário do Sul](https://www.centenariodosul.pr.gov.br/), tem por objetivo reunir todos caminhos de informação em apenas um local


<hr>

## 📟 Executar
### 📋 Pré-requisitos
* Python 3.8.2

### 🛠️ Configuração e Implantação
Crie um ambiente virtual:
```
python -m venv env
```
Efetue a atualização do pip
```
python -m pip install --upgrade pip
```
Ative o ambiente virtual e apos isso instale as bibliotecas do arquivo requirements.txt
```
pip install -r requirements.txt
```
Execute o comando de migração no terminal do ambiente virtural para criação das tabelas e do banco de dados.
```
python manage.py migrate
```

Crie um super usuario executando o comando e informe os dados solicitados.
```
python manage.py createsuperuser
```

Execute o comando abaixo:
```
python manage.py runserver
```
Este comando ira executar o sistema e estará acessivel via IP http://127.0.0.1:8000/ para os testes das funcionalidades.


## 🛠️ Construído com

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## ✒️ Autor
* **Desenvolvedor** - *Denis Muniz Silva* 

### 📞 Contatos
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://api.whatsapp.com/send?phone=5543991038557) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/denisms/) [![Email](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:denis.m.s.777@hotmail.com?) [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/de.muniz/) 
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/denisms3/) 
