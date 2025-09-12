from django.conf import settings
from django.contrib import admin
from .views import HomeTemplateView, IaTemplateView
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeTemplateView.as_view(), name='home'),
    path('ia/', IaTemplateView.as_view(), name='ia'),

    path('', include('curso.urls')),
    
    path('', include('identity.urls')),
    path('', include('events.urls')),
    path('', include('institutional.urls')),
    path('', include('generic.urls')),

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
