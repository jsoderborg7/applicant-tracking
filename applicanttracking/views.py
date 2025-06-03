
from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from itertools import chain

from .models import Applicants, Jobs, Skills

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "applicant_list"
    def get_queryset(self):
        return Applicants.objects.all()
    
