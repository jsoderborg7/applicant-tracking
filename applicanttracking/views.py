
from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from itertools import chain

from .models import Applicants, Jobs, Skills

class IndexView(generic.ListView):
    template_name = "index.html"
    def get_queryset(self):
        applicant_list = Applicants.objects.all()
        skill_list = Skills.objects.all()
        print(list(chain(applicant_list, skill_list)))
        return list(chain(applicant_list, skill_list))
    
