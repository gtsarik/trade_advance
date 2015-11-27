# -*- coding: utf-8 -*-
from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
# from django.core.urlresolvers import reverse

# from ..models import AboutUs


from django.shortcuts import render_to_response
from django.template import RequestContext

# from .models import Profile


def home_page(request):
    '''View for home page'''
    template = 'home.html'
    tiket_20 = 'Hello Word!'
    # profiles = Profile.objects.all()

    return render_to_response(
        template,
        {'tiket_20': tiket_20},
        context_instance=RequestContext(request))
