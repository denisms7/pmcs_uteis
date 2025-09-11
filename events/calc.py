from .models import Birthday, Holidays
from datetime import date

def get_events():
    events = []
    today = date.today()
    current_year = today.year

    # Aniversários - repetem todos os anos
    for b in Birthday.objects.all():
        # mantém mês e dia, atualiza ano para o ano atual
        birthday_this_year = b.birth.replace(year=current_year)
        events.append({
            "title": f"🎂 {b.name}",
            "start": birthday_this_year.isoformat(),
            "allDay": True,
            "color": "#0d6efd",
            "display": "background"  # opcional: destaca como background
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
