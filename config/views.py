from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class MagicView(TemplateView):
    template_name = 'show_magic.html'

class ExpView(TemplateView):
    template_name = 'exp.html'