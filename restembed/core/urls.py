from django.conf.urls import url
from . import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^set_index/$', views.set_index, name='set_index'),
    url(r'^create_set/$', views.create_set, name='create_set'),
]

