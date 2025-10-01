# PMCS Uteis
## 🚀 Pagina Web de atalhos e Informação 

Pagina web para auxilio dos servidores públicos do município de [Centenário do Sul](https://www.centenariodosul.pr.gov.br/), tem por objetivo reunir todos caminhos de informação em apenas um local

<hr>

## 📟 Executar
### 📋 Pré-requisitos
* Docker

### 🛠️ Configuração e Implantação
Configure o arquivo .env conforme o modelo .env.exemplo

Instale o Docker na maquina e rode  os seguintes  comando na  pasta raiz do projeto: 
```
docker compose build
```
```
docker compose up
```

Após os container subirem configure o Ngnix na que esta na porta 81 com usuário e senha padrão e adicione os seguintes locais nas configurações:
```
location /static/ {
    alias /var/www/staticfiles/;
    access_log off;
    expires 1y;
    add_header Cache-Control "public";
}
location /media/ {
    alias /var/www/media/;
    access_log off;
    expires 30d;
    add_header Cache-Control "public";
}
```

Crie um super usuario executando o comando abaixo dentro do container do Django e informe os dados solicitados.
```
python manage.py createsuperuser
```

O sistema esta pronto para ser utilizado.


## 🛠️ Construído com

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Postgress](https://img.shields.io/badge/postgress-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## ✒️ Autor
* **Desenvolvedor** - *Denis Muniz Silva* 

### 📞 Contatos
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://api.whatsapp.com/send?phone=5543991038557) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/denisms/) [![Email](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:denis.m.s.777@hotmail.com?) [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/de.muniz/) 
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/denisms3/) 
