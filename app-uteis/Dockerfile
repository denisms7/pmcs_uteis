# Imagem base do Python
FROM python:3.9

# Configuração do ambiente
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Diretório de trabalho no contêiner
WORKDIR /app-uteis

# Instalação das dependências do projeto
COPY requirements.txt /app-uteis/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o código do projeto para o contêiner
COPY . /app-uteis/

# Comandos para coletar arquivos estáticos e realizar as migrações do Django
RUN python manage.py collectstatic --no-input
RUN python manage.py migrate

# Instalar o Nginx
RUN apt-get update && apt-get install -y nginx

# Copiar o arquivo de configuração do Nginx
COPY nginx.conf /etc/nginx/sites-available/default

# Expor a porta 80 para o Nginx
EXPOSE 80

# Comando para iniciar o Nginx e o servidor de desenvolvimento do Django
CMD service nginx start && python manage.py runserver 0.0.0.0:8000
