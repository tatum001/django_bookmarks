import os.path 
from django.conf.urls.defaults import *
from bookmarks.views import *

site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
    ) 

urlpatterns = patterns('',
        (r'^$', main_page),
        (r'^user/(\w+)/$', user_page), 
    )



