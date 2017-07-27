from django.conf.urls import url
from mirror.views import *

urlpatterns = [
    # /mirror/
    url(r'^$', HomeView.as_view(), name='home'),

    # /mirror/create/
    url(r'^create/$', CalenderCreateFeed.as_view(), name='create'),

    #/mirror/2017/7/
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', CalenderMAV, name="list"),
]
