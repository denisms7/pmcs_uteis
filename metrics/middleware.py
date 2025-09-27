from .models import AnonymousVisit
from django.utils import timezone


class TrackAnonymousVisitsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Garante que a sessão existe
        if not request.session.session_key:
            request.session.create()

        session_key = request.session.session_key

        # Verifica se já existe visita hoje para essa sessão
        today = timezone.now().date()

        if not AnonymousVisit.objects.filter(session_key=session_key, timestamp__date=today).exists():
            AnonymousVisit.objects.create(session_key=session_key)

        response = self.get_response(request)
        return response
