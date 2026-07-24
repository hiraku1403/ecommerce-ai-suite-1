import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Se estiver rodando na Vercel, executa as migrações automaticamente no banco temporário
if os.getenv('VERCEL'):
    try:
        call_command('migrate', interactive=False)
    except Exception as e:
        print(f"Erro ao rodar auto-migrate na Vercel: {e}")

app = application