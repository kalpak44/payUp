from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'payUp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^page/', include('pages.urls', namespace="pages")),
	url(r'^auth/', include('logsys.urls', namespace="logsys")),
	url(r'^', include('pages.urls', namespace="pages")),
)