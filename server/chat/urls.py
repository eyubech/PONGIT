from django.urls import path
from . import views

urlpatterns = [
    path('/api/<str:sender_username>/<str:recipient_username>', views.chat_history, name='chat_history'),
]