from django.conf.urls.defaults import *
import be_dal.settings as settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^$', 'be_dal.views.index'),
  (r'^about/$', 'be_dal.views.about'),
  (r'^contact_us/$', 'be_dal.views.contact_us'),
  (r'^mobile/$', 'be_dal.views.mobile'),
  
#  (r'^products/$', 'be_dal._products.views.index'),
  (r'^products/(?P<product_id>\d)/(?P<product_title>.*)/$', 'be_dal._products.views.show'),
  (r'^products/(?P<query>.*\/)?$', 'be_dal._products.views.search'),
  
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
	
	(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
urlpatterns += patterns('',
    url(r'^captcha/', include('be_dal.captcha.urls')),
    url(r'^rosetta/', include('be_dal.rosetta.urls')),
)
