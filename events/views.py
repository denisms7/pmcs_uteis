from django.views.generic import TemplateView
from django.utils.timezone import now
from django.http import JsonResponse
from consulta.models import Consulta
from cadastros.models import Cadastro
from receita.models import Pedido
from django.utils.translation import get_language
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import timedelta
from notificacao.models import Notificacao


def adicionar_dias_uteis(data_inicial, dias_uteis):
    data = data_inicial
    dias_adicionados = 0

    while dias_adicionados < dias_uteis:
        data += timedelta(days=1)
        if data.weekday() < 5:  # Segunda a sexta (0 a 4)
            dias_adicionados += 1
    return data



def agendamentos_json(request):
    hoje = now()
    ano_atual = hoje.year
    notificacao = Notificacao.get_instance()

    # Todos os pedidos com envio e sem retorno
    pedidos_pendentes = Pedido.objects.filter(data_envio__isnull=False, data_retorno__isnull=True)

    consultas = Consulta.objects.exclude(data__isnull=True)
    aniversarios = Cadastro.objects.filter(
        status=1,
        nascimento__isnull=False
    )

    eventos = []
    prazo_laboratorio = int(notificacao.pazo_retorno)

    # Adiciona todos os prazos de pedidos pendentes
    for pedido in pedidos_pendentes:
        try:
            data_prazo = adicionar_dias_uteis(pedido.data_envio, prazo_laboratorio)
            eventos.append({
                "title": f"👓 {pedido.cadastro.primeiro_nome} {pedido.cadastro.ultimo_nome}",
                "start": data_prazo.isoformat(),
                "end": data_prazo.isoformat(),
                "color": "#fd7e14",
            })
        except Exception:
            continue  # Ignora pedidos com erro no cálculo

    # Datas de consulta
    for consulta in consultas:
        eventos.append({
            "title": f"👩‍⚕️ {consulta.cidade}",
            "start": consulta.data.isoformat(),
            "end": consulta.data.isoformat(),
            "color": "#67aaf1",
        })

    # Aniversários
    for cad in aniversarios:
        try:
            aniversario_ano = cad.nascimento.replace(year=ano_atual)
        except ValueError:
            aniversario_ano = cad.nascimento.replace(year=ano_atual, day=28)

        eventos.append({
            "title": f"🎂 {cad.primeiro_nome}",
            "start": aniversario_ano.isoformat(),
            "end": aniversario_ano.isoformat(),
            "color": "#17a2b8",
        })

    return JsonResponse(eventos, safe=False)


class CalendarioView(LoginRequiredMixin, TemplateView):
    template_name = 'calendario/calendario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGE_CODE'] = get_language()
        return context
