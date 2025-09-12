from django.views.generic.list import ListView
from .models import Legislation


class LegislationListView(ListView):
    model = Legislation
    template_name = 'generic/legislation.html'
    context_object_name = 'legislation'

    def get_queryset(self):
        self.type_param = self.kwargs.get("type")

        queryset = super().get_queryset().filter(
            category=self.type_param,
            active=True
        )

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["legislation"]:
            context["category_display"] = context["legislation"][0].get_category_display()
        return context
