# Usa uma imagem base do Python
FROM python:3.11

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Django
RUN pip install -r requirements.txt

# Copia o restante do projeto para o diretório de trabalho
COPY . .

# Expõe a porta 80 (ou qualquer porta usada pelo Django)
EXPOSE 80

# Inicia o servidor do Django
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:80
