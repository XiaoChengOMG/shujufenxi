from django.conf.urls import patterns, include, url

from django.contrib import admin
import mysite.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', mysite.views.index),
    url(r'^xsck/', mysite.views.xsck),
    url(r'', mysite.views.login1),
    url(r'login', mysite.views.login),

)
