# -*- coding: utf-8 -*-

#   Copyright (c) 2011, BE-DAL Inc.  sSee
#   the COPYRIGHT file.

import datetime
from django.db import models

class Product(models.Model):
  photo = models.ImageField("A 614x298 photo", upload_to="products/")
  title = models.CharField(max_length=60)
  info = models.TextField(blank=True, null=True)
  url = models.CharField(max_length=70)
  price = models.IntegerField(max_length=6)
  date = models.DateTimeField(default=datetime.datetime.now)
  
  def __unicode__(self):
    return self.title
  
  def exists(self, product_id):
    try:
      Product.objects.get(id=product_id)
    except:
      return False
    return True
