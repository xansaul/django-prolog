from django.http import JsonResponse
from rest_framework.views import APIView

from chatbot.chatbotapi.serializers import QuestionSerializer

from .prolog.helpers import find_similar_question
from .prolog.questions import questions
from .prolog.PrologUseCase import PrologUseCase

import os


class ChatbotView(APIView):

    def post(self, request):

        serialized_data = QuestionSerializer(data=request.data)

        if not serialized_data.is_valid():
            return JsonResponse(serialized_data.errors, status=400)

        question = find_similar_question(serialized_data.data.get('question'), questions)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        prolog_file_path = os.path.join(current_directory, 'prolog', 'bot.pl')
        prolog_file_path = prolog_file_path.replace("\\", "/")

        response = PrologUseCase(prolog_file_path).make_question(question)

        return JsonResponse({
            'bot': response
        })
