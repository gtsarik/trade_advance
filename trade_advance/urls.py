from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # home urls
    url(r'^$', 'apps.computer_firm.views.home_page', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
