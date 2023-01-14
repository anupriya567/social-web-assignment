from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . serializers import MessageSerializer,LikeMessageSerializer
from . models import Message, LikeMessage
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class MessageVS(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['sender']
    
    def create(self, request, *args, **kwargs):
        message = request.data
        user = request.user
                  
        serializer = MessageSerializer(data = message)
        if serializer.is_valid():
            message = Message.objects.create(**serializer.validated_data, sender = user)
            message.save()
            return Response(MessageSerializer(message).data)
        return Response(serializer.errors)  

class LikeMessageView(APIView):

     def get(self,request,pk):
        message = Message.objects.get(pk = pk)
        like = LikeMessage.objects.filter(message = message, user = request.user)
        
        if not like:
            message.no_of_likes = message.no_of_likes + 1
            message.save()
            likemsg = LikeMessage.objects.create(message = message, user = request.user)
            likemsg.save() 

            serializer = LikeMessageSerializer(likemsg)
            return Response(serializer.data) 

             

        return Response( {"error": "already liked the message"}, status=status.HTTP_400_BAD_REQUEST)      

               
    
      