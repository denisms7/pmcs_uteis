from django.views.generic.list import ListView
from django.db.models import Q
from unidecode import unidecode
from .models import Schedule, OfficialAddress


class ContactsListView(ListView):
    model = Schedule
    template_name = 'contacts/index.html'
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')

        # Normaliza a query para ignorar acentos
        query_normalized = unidecode(query) if query else ''

        if query_normalized:
            queryset = queryset.filter(
                Q(person__icontains=query_normalized) | 
                Q(internal_number__icontains=query_normalized) | 
                Q(address__phone__icontains=query_normalized)
            )
        return queryset


class ExportListView(ListView):
    model = Schedule
    template_name = 'contacts/export.html'
    context_object_name = "contacts"


class AddressesListView(ListView):
    model = OfficialAddress
    template_name = 'addresses/index.html'
    context_object_name = "address"
