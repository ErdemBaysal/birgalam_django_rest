from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from st_api.views import FeedListViewSet,FeedDetailViewSet, api_root, FeedRatingViewSet
from rest_framework import renderers

feeds_list = FeedListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
feeds_detail = FeedDetailViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
"""user_list = UserViewSet.as_view({
    'get': 'list'
})"""
feedrating_list = FeedRatingViewSet.as_view({
    'get': 'list',
    #'post': 'create'
})
feedrating_detail = FeedRatingViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^feeds/$', feeds_list, name='feeds-list'),
    url(r'^feeds/(?P<pk>[0-9]+)/$', feeds_detail, name='feeds-detail'),
    url(r'^feedrating/$', feedrating_list, name='feedrating-list'),
   #url(r'^feededitor/(?P<pk>[0-9]+)/$', feededitor_detail, name='feededitor-detail'),
    #url(r'^users/$', user_list, name='user-list'),
    #url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])