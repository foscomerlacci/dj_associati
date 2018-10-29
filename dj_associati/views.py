# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Socio,
	Disciplina,
)


class SocioCreateView(CreateView):

    model = Socio


class SocioDeleteView(DeleteView):

    model = Socio


class SocioDetailView(DetailView):

    model = Socio


class SocioUpdateView(UpdateView):

    model = Socio


class SocioListView(ListView):

    model = Socio


class DisciplinaCreateView(CreateView):

    model = Disciplina


class DisciplinaDeleteView(DeleteView):

    model = Disciplina


class DisciplinaDetailView(DetailView):

    model = Disciplina


class DisciplinaUpdateView(UpdateView):

    model = Disciplina


class DisciplinaListView(ListView):

    model = Disciplina

