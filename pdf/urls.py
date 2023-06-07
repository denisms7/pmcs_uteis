from django.urls import path
from .views import upload_and_merge_pdf, split_pdf, download_zip


urlpatterns = [
    path('juntarPDF', upload_and_merge_pdf, name='upload_pdf'),
    path('separarPDF/', split_pdf, name='split_pdf'),
    path('download_zip/<str:session_id>/', download_zip, name='download_zip'),
]
