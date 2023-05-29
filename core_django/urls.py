from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('', include('cursos.urls')),
]


handler400 = 'paginas.views.error_400_view'
handler403 = 'paginas.views.error_403_view'
handler404 = 'paginas.views.error_404_view'
handler500 = 'paginas.views.error_500_view'
handler502 = 'paginas.views.error_502_view'