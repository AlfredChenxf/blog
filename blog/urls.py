from django.conf.urls import patterns, include, url
from django.contrib import admin
from firstBlog.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^latest/$', latest_book),
    url(r'^blog/$', blog),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
)
