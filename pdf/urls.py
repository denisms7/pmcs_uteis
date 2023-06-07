from django.urls import path
from .views import merge_pdf, split_pdf, download_zip


urlpatterns = [
    path('', merge_pdf, name='marge_pdf'),
    path('separarPDF/', split_pdf, name='split_pdf'),
    path('download_zip/<str:session_id>/', download_zip, name='download_zip'),
]
