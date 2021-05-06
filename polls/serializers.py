from rest_framework import serializers

from polls.models import Polls, Question, Answer, UserStatistic


class PollsListSerializers(serializers.ModelSerializer):
    """Список опросов"""

    class Meta:
        model = Polls
        fields = '__all__'


class AnswerSerializers(serializers.ModelSerializer):
    """Список ответов"""

    class Meta:
        model = Answer
        exclude = ('question',)


class QuestionSerializers(serializers.ModelSerializer):
    """Вопросы"""

    options = AnswerSerializers(many=True)

    class Meta:
        model = Question
        fields = ('id', 'name', 'type', 'options')


class AnswerSaveSerializers(serializers.ModelSerializer):
    """Сохранение ответа пользователя"""

    class Meta:
        model = UserStatistic
        fields = '__all__'


class AnswerUserSerializers(serializers.ModelSerializer):
    """Ответы пользователя"""

    class Meta:
        model = UserStatistic
        fields = ('id', 'answer')


class QuestionStaticSerializers(serializers.ModelSerializer):
    """Вопросы с приязкой к статистике ответов"""

    answer_user = AnswerUserSerializers(many=True)

    class Meta:
        model = Question
        fields = ('id', 'name', 'type', 'answer_user')


class PollsSerializers(serializers.ModelSerializer):
    """Список опросов с данными ответов пользователей"""

    questions = QuestionStaticSerializers(many=True)

    class Meta:
        model = Polls
        fields = ('id', 'name', 'from_date', 'to_date',
                  'description', 'questions')
