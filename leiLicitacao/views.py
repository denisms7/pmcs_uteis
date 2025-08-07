from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import pandas as pd
from django.conf import settings
from datetime import datetime
from django.shortcuts import render
import os


class LicitacaoAjuda(TemplateView):
    template_name = 'leiLicitacao/index.html'

