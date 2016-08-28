from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pokemonGo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'search.views.index', name='index'),
    #url(r'^pokemon$', 'search.views.index', name = 'index'),
    url(r'^random$', 'search.views.random', name = 'random'),
    url(r'^searchGET$', 'search.views.srchget', name = 'search'),
    url(r'^searchPOST$', 'search.views.srchpost', name = 'searchPOST'),
    #un-named grouping
    url(r'^edit/(\d+)', 'search.views.edit', name = 'Edit'),
    #named-grouping
    #url(r'^search/(?P<foo>\d+)', 'search.views.srch2', name = 'search2'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),

    url(r'^register/$', 'search.views.register', name='register'),
    url(r'^login/$', 'search.views.user_login', name='login'),
    
    url(r'^searchREDIRECT/(?P<search_string>[\*\w\-]+)/$', 'search.views.srchredirect', name = 'searchredirect'),
)
