from rest_framework import serializers

class PlayMobileSerializer(serializers.Serializer):
    message_id = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=12)
    text = serializers.CharField(max_length=255)