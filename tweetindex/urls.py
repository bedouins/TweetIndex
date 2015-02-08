from django.conf.urls import patterns

from db.views import api

urlpatterns = patterns('',
    (r'^$', api),
)
