web: gunicorn api_paciente.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn  api_paciente.wsg