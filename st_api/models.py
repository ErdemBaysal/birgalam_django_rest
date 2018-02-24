from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	category=models.CharField(max_length=100, blank=True)
	title = models.TextField(blank=True)
	detail = models.TextField(blank=True)
	publish_date = models.DateTimeField(null = True)
	body = models.TextField(blank=True)
	url = models.CharField(max_length=500, blank=True)
	creator = models.ForeignKey('auth.User', related_name='feeds', on_delete=models.CASCADE) #user who inserted the feed
	label = models.CharField(max_length=10,blank=True)

	class Meta:
		ordering = ('created',)
		db_table = "st_feeds"


class FeedRating(models.Model):
	rate = models.CharField(max_length=1,null=True)
	created = models.DateTimeField(auto_now_add=True)
	feed = models.ForeignKey(Feed,related_name='rated_editors', on_delete=models.CASCADE)
	editor = models.ForeignKey('auth.User', related_name='editors', on_delete=models.CASCADE)

	class Meta:
		ordering = ('created',)
		db_table = "st_feed_ratings"