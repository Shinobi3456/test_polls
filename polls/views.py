import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Polls, Question
from polls.serializers import PollsListSerializers, QuestionSerializers, AnswerSaveSerializers, PollsSerializers


class PollsList(APIView):
    """Список доступных опросов на текущую дату"""

    def get(self, request):
        objects = Polls.objects.filter(from_date__lte=datetime.datetime.today(),
                                       to_date__gte=datetime.datetime.today()).all()
        serializer = PollsListSerializers(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PollsDetail(APIView):
    """Список вопросов в опросе"""

    def get(self, request, polls_id):
        objects = Question.objects.filter(polls_id=polls_id, draft=False).all()
        serializer = QuestionSerializers(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerSaveView(APIView):
    """Сохраение ответа пользователя"""

    def post(self, request):
        serializer = AnswerSaveSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})


class StatisticUserViewView(APIView):
    """Статистика ответов пользователя"""

    def get(self, request, user_id):
        polls = Polls.objects.raw(
            """SELECT polls_polls.* FROM polls_polls
                JOIN polls_question ON polls_polls.id = polls_question.polls_id
                JOIN polls_userstatistic pu ON polls_question.id = pu.question_id
            WHERE pu.user_id=%s
            GROUP BY polls_polls.id""", [user_id])

        serializer = PollsSerializers(polls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
