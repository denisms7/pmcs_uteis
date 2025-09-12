from django.urls import path
from .views import ContactsListView, ExportListView, AddressesListView


urlpatterns = [
    path('contatos/', ContactsListView.as_view(), name='contacts_'),
    path('contatos/agenda/', ExportListView.as_view(), name='contacts_export'),

    path('enderecos.oficiais/', AddressesListView.as_view(), name='addresses_'),
]
