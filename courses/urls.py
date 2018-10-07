from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses.views import hello_word_view, index, contacts


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'courses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='index'),
    url(r'^contacts/$', contacts, name='our_contacts'),
    url(r'^hello/(?P<name>\d+)/$', hello_word_view, name='hello'),
    url(r'^admin/', include(admin.site.urls)),
)
