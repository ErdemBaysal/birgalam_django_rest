from rest_framework import serializers
from st_api.models import Feed, FeedRating
from django.contrib.auth.models import User

class FeedRatingSerializer(serializers.ModelSerializer):
	editor = serializers.ReadOnlyField(source='editor.username')
	class Meta:
		model = FeedRating
		fields = ('id','rate','created','feed','editor')

class FeedListSerializer(serializers.ModelSerializer):

	rated_editors = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='editor_id'
	 )
	class Meta:
			model = Feed
			fields = ('id', 'created', 'category','title', 'detail', 'publish_date', 'body', 'url','label', 'rated_editors')
			read_only_fields = ('id', 'created')

	def create(self, validated_data):
		return Feed.objects.create(**validated_data)

class FeedDetailSerializer(serializers.ModelSerializer):
	
	inrate = serializers.CharField(write_only=True)
	def validate_inrate(self, value):
		"""
		Check if input rate is valid
		"""
		if value not in ('1','2','3','4'):
			raise serializers.ValidationError("Rate must be between 1 and 4")
		return value
	
	class Meta:
		model = Feed
		fields = ('id', 'created', 'category','title', 'detail', 'publish_date', 'body', 'url','inrate')
		read_only_fields = ('id', 'created')

	def update(self, instance, validated_data):
		#Create an feedrating instance while updating the feed instance
		feed_instance=Feed.objects.get(pk=instance.id)
		obj = FeedRating.objects.create(feed=feed_instance, editor=validated_data.get('editor'), rate=validated_data.get('inrate'))
		obj.save()

		instance.save()
		return instance