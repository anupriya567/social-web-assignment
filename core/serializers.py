from .models import Message, LikeMessage
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    
    sender = serializers.StringRelatedField( read_only = True)
    likes = serializers.StringRelatedField(many=True, read_only = True)
    class Meta:
        model = Message
        fields = '__all__'

class LikeMessageSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField( read_only = True)
    message = serializers.StringRelatedField( read_only = True)
    class Meta:
        model = LikeMessage
        fields = '__all__'
