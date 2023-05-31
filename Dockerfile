# Base image
FROM python:3.9

# Define a pasta de trabalho dentro do container
WORKDIR /pmcs_uteis

# Copie o arquivo requirements.txt para o container
COPY requirements.txt .

# Instale as dependências do Django
RUN pip install -r requirements.txt

# Copie o restante do código fonte para o container
COPY . .

# Defina as variáveis de ambiente necessárias para a aplicação Django
ENV DJANGO_SETTINGS_MODULE=core_django.settings
ENV PYTHONUNBUFFERED=1


# Execute as migrações do Django
RUN python manage.py migrate

# Exponha a porta necessária para acessar a aplicação
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
