from django.shortcuts import render
from st_api.models import Feed,FeedRating
from django.contrib.auth.models import User
from st_api.serializers import FeedListSerializer,FeedDetailSerializer, FeedRatingSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		#'users': reverse('user-list', request=request, format=format),
		'feeds': reverse('feeds-list', request=request, format=format),
		'feedrating': reverse('feedrating-list', request=request, format=format)
	})

class FeedListViewSet(viewsets.ModelViewSet):
	"""
	For list view and create purposes
	"""
	permission_classes = (DjangoModelPermissions,)
	serializer_class = FeedListSerializer
	def get_queryset(self):
		user=self.request.user.id,
		feed_list=list(FeedRating.objects.filter(editor_id=user).values_list('feed_id',flat=True))	
		return Feed.objects.exclude(id__in=feed_list)

	def perform_create(self, serializer):
		user=self.request.user
		serializer.save(creator=user)

class FeedDetailViewSet(viewsets.ModelViewSet):
	"""
	For individual feed view and update purposes
	"""
	permission_classes = (DjangoModelPermissions,)
	serializer_class = FeedDetailSerializer
	def get_queryset(self):
		user=self.request.user.id,
		feed_list=list(FeedRating.objects.filter(editor_id=user).values_list('feed_id',flat=True))	
		return Feed.objects.exclude(id__in=feed_list)

	def perform_create(self, serializer):
		user=self.request.user
		serializer.save(creator=user)
	
	def perform_update(self, serializer):
		user=self.request.user
		serializer.save(editor=user)

class FeedRatingViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list` actions
	"""
	permission_classes = (DjangoModelPermissions,)
	queryset = FeedRating.objects.all()
	serializer_class = FeedRatingSerializer
	def perform_create(self, serializer):
		user=self.request.user
		serializer.save(editor=user)
