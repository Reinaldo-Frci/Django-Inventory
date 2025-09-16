from django.contrib import admin
from .models import *

# Register your models here.
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'qtd','nome', 'marca', 'modelo', 'local', 'status')

class CaboAdmin(admin.ModelAdmin):
    list_display = ('id', 'qtd','tipo', 'comprimento', 'local', 'status')

class CaboInline(admin.StackedInline):
    model = Cabo
    can_delete = False

class EquipamentoInline(admin.StackedInline):
    model = Equipamento
    can_delete = False




admin.site.register(Equipamento, EquipamentoAdmin )
admin.site.register(Cabo, CaboAdmin)
admin.site.register(Local, inlines = [CaboInline.q, EquipamentoInline])