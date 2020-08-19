from django.conf.urls import url
from AppNumber4 import views

# TEMPLATE TAGGING
app_name = 'AppNumber4'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]