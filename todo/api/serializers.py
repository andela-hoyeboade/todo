from bucket.models import Bucketlist
from rest_framework import serializers


class BucketlistSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
