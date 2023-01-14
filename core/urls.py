from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

message_router = DefaultRouter()
message_router.register('',views.MessageVS,basename="message")

urlpatterns = [
    path('messages/', include(message_router.urls)),
    path("like/message/<int:pk>", views.LikeMessageView.as_view(), name = "like-message")


]
