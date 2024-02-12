from rest_framework import serializers

from rest_framework import serializers

class LinkSerializer(serializers.Serializer):
   url = serializers.CharField()