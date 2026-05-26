from django.contrib import admin
from .models import Evento, Presenca, Comentario

admin.site.site_header = "UniConnect Recife Admin"
admin.site.site_title = "UniConnect Recife"
admin.site.index_title = "Painel Administrativo"

admin.site.register(Evento)
admin.site.register(Presenca)
admin.site.register(Comentario)