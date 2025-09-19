from django.contrib import admin
from transaction.models import LogMudarLocal, LogSaida

# Register your models here.

admin.site.register(LogMudarLocal)
admin.site.register(LogSaida)
