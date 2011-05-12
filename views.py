# -*- coding: utf-8 -*-

#   Copyright (c) 2011, BE-DAL Inc.  See
#   the COPYRIGHT file.

# django
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import *
from django.core.mail import mail_admins

# be_dal
from be_dal._products.models import Product
from be_dal.forms import ContactForm
from be_dal.django_mobile import *


@csrf_protect
def index(request):
  products = Product.objects.order_by('-id')[0:10]
  return render_to_response("templates/index.html", {'products':products},
  context_instance=RequestContext(request))

@csrf_protect
def about(request):
  return render_to_response("templates/about.html", {},
  context_instance=RequestContext(request))

@csrf_protect
def contact_us(request):
  form = ContactForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      cd = form.cleaned_data
      message = """
BE DAL - Email 
email: %s<br>
name: %s<br>
message: %s<br><br><br>
Answer by sending an email at : %s
      """ % (cd['email'], cd['name'], cd['message'], cd['email'])
      mail_admins(
        cd['subject'], message,
      )
      return HttpResponseRedirect('/')
  else:
    form = ContactForm()
  
  return render_to_response("templates/contact_us.html", {'form':form},
  context_instance=RequestContext(request))

# a simple page
@csrf_protect
def mobile(request):
  if get_flavour(request) == 'mobile':
    return HttpResponseRedirect('/')
  return render_to_response("templates/mobile.html", {},
  context_instance=RequestContext(request))
