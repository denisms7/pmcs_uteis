from django.http import JsonResponse
from .models import Birthday, Holidays
from datetime import date

def get_events():
    events = []

    # Aniversários
    for b in Birthday.objects.all():
        events.append({
            "title": f"🎂 {b.name}",
            "start": b.birth.strftime("%Y-%m-%d"),
            "allDay": True,
            "color": "#0d6efd"
        })

    # Feriados
    for h in Holidays.objects.all():
        events.append({
            "title": f"📅 {h.name}",
            "start": h.date.strftime("%Y-%m-%d"),
            "allDay": True,
            "color": "#dc3545"
        })

    return JsonResponse(events, safe=False)
