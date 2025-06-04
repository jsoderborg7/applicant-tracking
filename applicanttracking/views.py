
from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from itertools import chain

from .models import Applicants, Jobs, Skills

class IndexView(generic.ListView):
    model = Applicants
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Jobs.objects.all()
        context['skills'] = Skills.objects.all()
        context['unique_skills'] = Skills.objects.values_list('name', flat=True).distinct()
        context['applicants'] = Applicants.objects.all()
        return context
