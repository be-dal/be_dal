# -*- coding: utf-8 -*-

#   Copyright (c) 2011, BE-DAL Inc.  See
#   the COPYRIGHT file.

# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# be_dal
from be_dal.captcha.fields import CaptchaField

class ContactForm(forms.Form):
  email = forms.EmailField(label=_(u'Your email'),
    error_messages = {'invalid': _("This should be an email address"),
    'required': _("Your email is required")})
  name = forms.CharField(label=_(u'Your name'),
	  error_messages = {'required': _("Your name is required")})
  subject = forms.CharField(label=_(u'Subject'),
    error_messages = {'required': _("A subject is required")})
  message = forms.CharField(widget=forms.Textarea)
  captcha = CaptchaField(label=_(u'Security test'))
