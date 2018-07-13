from django.conf.urls import include, url
from django.contrib import admin
from services import views
from services.views import *
# from letschat import urls


urlpatterns = [
    url(r'^', ChatterBotAppView.as_view(), name='main'),
    # url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^blog/$', myconvfun , name='chatterbot'),
]
