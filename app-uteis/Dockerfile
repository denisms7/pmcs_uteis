# Imagem base do Python
FROM python:3.11

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

# Instalar o Nginx
RUN apt-get update && apt-get install -y nginx

# Copiar o arquivo de configuração do Nginx
COPY nginx.conf /etc/nginx/sites-available/default


# Comandos para coletar arquivos estáticos e realizar as migrações do Django
RUN python manage.py collectstatic --no-input
RUN python manage.py migrate

# O valor 555 representa as permissões de somente leitura
# O valor 755 proprietário do arquivo leitura, demais usuario somente leitura 

# Definir permissões adequadas para a pasta staticfiles
RUN chmod -R 755 /app-uteis/staticfiles
RUN chown -R www-data:www-data /app-uteis/staticfiles

# Definir permissões adequadas para a pasta media
RUN chmod -R 755 /app-uteis/media
RUN chown -R www-data:www-data /app-uteis/media

# Definir permissões adequadas para a pasta paginas
RUN chmod -R 555 /app-uteis/paginas

# Definir permissões adequadas para a pasta core_django
RUN chmod -R 555 /app-uteis/core_django

# Definir permissões adequadas para a pasta curso
RUN chmod -R 555 /app-uteis/curso

# Definir permissões adequadas para a pasta pdf_ferramentas
RUN chmod -R 755 /app-uteis/pdf_ferramentas
RUN chown -R www-data:www-data /app-uteis/pdf_ferramentas

# Definir permissões adequadas para a pasta templates
RUN chmod -R 555 /app-uteis/templates


# Expor a porta 80 para o Nginx
EXPOSE 80

# Comando para iniciar o Nginx e o servidor de desenvolvimento do Django
CMD service nginx start && python manage.py runserver 0.0.0.0:8000
