from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^', include('st_api.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]

