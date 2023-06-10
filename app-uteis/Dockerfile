# Imagem base do Python
FROM python:3.9

# Configuração do ambiente
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Diretório de trabalho no contêiner
WORKDIR /code

# Instalação das dependências do projeto
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o código do projeto para o contêiner
COPY . /code/

# Comandos para coletar arquivos estáticos e realizar as migrações do Django
RUN python manage.py collectstatic --no-input
RUN python manage.py migrate

# Porta que será exposta no contêiner
EXPOSE 8000

# Comando para executar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
