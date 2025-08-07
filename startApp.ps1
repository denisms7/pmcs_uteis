# Navega at  o diret rio do projeto Django
cd D:\pmcs

# Ativa o ambiente virtual
. .\env\Scripts\Activate.ps1

# Inicializa o servidor Django
py manage.py runserver 192.168.1.1:8092
ou
gunicorn meu_projeto.wsgi:application --bind 0.0.0.0:8000
