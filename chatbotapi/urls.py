from django.urls import path

from chatbot.chatbotapi.views import ChatbotView

urlpatterns = [
    path('chatbot', ChatbotView.as_view(), name='chat_bot')
]
