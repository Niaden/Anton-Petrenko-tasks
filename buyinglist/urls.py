from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'secondapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', 'buyinglist.views.tobuy'),
)
