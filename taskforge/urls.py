from django.contrib import admin
from django.urls import path

from core.views import (
    home,
    criar_evento,
    confirmar_presenca,
    comentar
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('criar-evento/', criar_evento, name='criar_evento'),

    path(
        'confirmar-presenca/<int:evento_id>/',
        confirmar_presenca,
        name='confirmar_presenca'
    ),

    path(
        'comentar/<int:evento_id>/',
        comentar,
        name='comentar'
    ),
]