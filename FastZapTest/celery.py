import os
from celery import Celery
from django.conf import settings

# integrando o celery com o django (indicando o módulo settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FastZapTest.settings")
app = Celery("FastZapTest")

# permitindo o celery se auto configurar apartir das confs do settings django
app.config_from_object("django.conf:settings", namespace="CELERY")
# serve pra ele saber onde estão os módulos pra ele procurar por tarefas automaticamente

# app.conf.beat_schedule = {
#     "create-rf003": {
#         # path para a task
#         "task": "",
#         "schedule": #definir tempo,
#     }
# }

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)