from django.contrib import admin

from .models import *

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')


admin.site.register(Negocio)
admin.site.register(Reserva)
admin.site.register(Posteo)
admin.site.register(Tarifa)