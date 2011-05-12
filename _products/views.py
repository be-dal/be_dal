# -*- coding: utf-8 -*-

#   Copyright (c) 2011, BE-DAL Inc.  sSee
#   the COPYRIGHT file.

# django
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import *
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# be_dal
from be_dal._products.models import Product

@csrf_protect
def show(request, product_id, product_title=None):
  if not Product().exists(product_id):
    return HttpResponseRedirect('/')
  product = Product.objects.get(id=product_id)
  product.photo_width = product.photo.width
  if product.photo.width > 918:
    product.photo_width = 918
  return render_to_response("_products/templates/show.html", {'product':product},
  context_instance=RequestContext(request))

# search() is also the index()
# function for displaying the products
@csrf_protect
def search(request, query=None):
  if query is None:
    query = request.GET.get('q', '')
	
  # search ...
  qset = (
    Q(title__icontains=query) |
    Q(info__icontains=query) |
    Q(price__icontains=query)
  )
  if query:
    results = Product.objects.filter(qset).distinct().order_by("title")
  else:
    results = Product.objects.all().distinct().order_by("title")
    query = _('Products')
  
  if results.count() == 1:
    for r in results:
      return HttpResponseRedirect('/products/%s/%s/' % (r.id, r.url) )
  
  for r in results:
    if r.photo.width > 600:
      r.photo_width = 600
    if r.photo.height > 250:
      r.photo_width = (r.photo.width * 1.0 / r.photo.height) * 250
  
  return render_to_response("_products/templates/search.html",
  {'results':results, 'query': query},
  context_instance=RequestContext(request))
