# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'dj_associati'
urlpatterns = [
    url(
        regex="^Socio/~create/$",
        view=views.SocioCreateView.as_view(),
        name='Socio_create',
    ),
    url(
        regex="^Socio/(?P<pk>\d+)/~delete/$",
        view=views.SocioDeleteView.as_view(),
        name='Socio_delete',
    ),
    url(
        regex="^Socio/(?P<pk>\d+)/$",
        view=views.SocioDetailView.as_view(),
        name='Socio_detail',
    ),
    url(
        regex="^Socio/(?P<pk>\d+)/~update/$",
        view=views.SocioUpdateView.as_view(),
        name='Socio_update',
    ),
    url(
        regex="^Socio/$",
        view=views.SocioListView.as_view(),
        name='Socio_list',
    ),
	url(
        regex="^Disciplina/~create/$",
        view=views.DisciplinaCreateView.as_view(),
        name='Disciplina_create',
    ),
    url(
        regex="^Disciplina/(?P<pk>\d+)/~delete/$",
        view=views.DisciplinaDeleteView.as_view(),
        name='Disciplina_delete',
    ),
    url(
        regex="^Disciplina/(?P<pk>\d+)/$",
        view=views.DisciplinaDetailView.as_view(),
        name='Disciplina_detail',
    ),
    url(
        regex="^Disciplina/(?P<pk>\d+)/~update/$",
        view=views.DisciplinaUpdateView.as_view(),
        name='Disciplina_update',
    ),
    url(
        regex="^Disciplina/$",
        view=views.DisciplinaListView.as_view(),
        name='Disciplina_list',
    ),
	]
