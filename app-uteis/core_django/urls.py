from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('', include('curso.urls')),
    path('', include('pdf_ferramentas.urls')),
    path('', include('agenda.urls')),
    path('', include('leiLicitacao.urls')),
    path('', include('agenda_externa.urls')),
]



'''
handler400 = 'paginas.views.error_400_view'
handler403 = 'paginas.views.error_403_view'
handler404 = 'paginas.views.error_404_view'
handler500 = 'paginas.views.error_500_view'
handler502 = 'paginas.views.error_502_view'
'''

# Configuração das URLs de mídia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
