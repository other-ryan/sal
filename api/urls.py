from django.conf.urls import *

urlpatterns = patterns('api.views',
    (r'^v1/machines/$', 'v1_machines'),
    (r'^v1/newmachine/$','v1_create_machine'),
)