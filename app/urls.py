from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import HomeTemplateView
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', HomeTemplateView.as_view(), name='home'),
    path('', include('curso.urls')),
    path('', include('identity.urls')),
    path('', include('events.urls')),
    path('', include('institutional.urls')),
    path('', include('generic.urls')),
    path('', include('metrics.urls')),
]

# Configuração das URLs de mídia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
