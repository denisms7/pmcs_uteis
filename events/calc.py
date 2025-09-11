from .models import Birthday, Holidays

def get_events():
    events = []

    # Aniversários
    for b in Birthday.objects.all():
        events.append({
            "title": f"🎂 {b.name}",
            "start": b.birth.isoformat(),
            "allDay": True,
            "color": "#0d6efd",
        })

    # Feriados
    for h in Holidays.objects.all():
        events.append({
            "title": f"📅 {h.name}",
            "start": h.date.isoformat(),
            "allDay": True,
            "color": "#dc3545",
        })

    return events
