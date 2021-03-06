from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from week2.views import echo_get, video_handler

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mobilecloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'1-SimpleServlet/echo', echo_get),
    url(r'2-VideoServlet/video', video_handler),
)
