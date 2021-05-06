import datetime

from django.test import TestCase

import polls.models as models


class PollsModelTest(TestCase):
    """Тесты для модели опросов"""

    @classmethod
    def setUpTestData(cls):
        cls.obj = models.Polls.objects.create(name='Тестовый опрос',
                                              from_date=datetime.datetime.strptime(
                                                  '04.05.2021', '%d.%m.%Y'),
                                              to_date=datetime.datetime.strptime(
                                                  '07.05.2021', '%d.%m.%Y'),
                                              description='тестовое описание')

    def test_name_label(self):
        polls_model = models.Polls.objects.get(id=self.obj.id)
        field_label = polls_model._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_from_date_label(self):
        polls_model = models.Polls.objects.get(id=self.obj.id)
        field_label = polls_model._meta.get_field('from_date').verbose_name
        self.assertEquals(field_label, 'Дата старта')

    def test_to_date_label(self):
        polls_model = models.Polls.objects.get(id=self.obj.id)
        field_label = polls_model._meta.get_field('to_date').verbose_name
        self.assertEquals(field_label, 'Дата окончания')

    def test_description_label(self):
        polls_model = models.Polls.objects.get(id=self.obj.id)
        field_label = polls_model._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_name_max_length(self):
        polls_model = models.Polls.objects.get(id=self.obj.id)
        max_length = polls_model._meta.get_field('name').max_length
        self.assertEquals(max_length, 250)

    def test_description_max_length(self):
        polls_model = models.Polls.objects.get(id=self.obj.id)
        max_length = polls_model._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    def test_object_name_is_name_and_dates(self):
        polls_model = models.Polls.objects.get(id=self.obj.id)
        expected_object_name = f'{polls_model.name} ' \
                               f'{polls_model.from_date.strftime("%d.%m.%Y")}-' \
                               f'{polls_model.to_date.strftime("%d.%m.%Y")}'
        self.assertEquals(expected_object_name, str(polls_model))


class QuestionModelTest(TestCase):
    """Тесты для модели вопросов"""

    @classmethod
    def setUpTestData(cls):
        poll = models.Polls.objects.create(name='Тестовый опрос',
                                           from_date=datetime.datetime.strptime(
                                               '04.05.2021', '%d.%m.%Y'),
                                           to_date=datetime.datetime.strptime(
                                               '07.05.2021', '%d.%m.%Y'),
                                           description='тестовое описание')

        cls.obj = models.Question.objects.create(polls=poll,
                                                 name='Тестовый вопрос',
                                                 type='1',
                                                 draft=False)

    def test_polls_label(self):
        question_model = models.Question.objects.get(id=self.obj.id)
        field_label = question_model._meta.get_field('polls').verbose_name
        self.assertEquals(field_label, 'Опрос')

    def test_name_label(self):
        question_model = models.Question.objects.get(id=self.obj.id)
        field_label = question_model._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Текст вопроса')

    def test_type_label(self):
        question_model = models.Question.objects.get(id=self.obj.id)
        field_label = question_model._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'Тип вопроса')

    def test_draft_label(self):
        question_model = models.Question.objects.get(id=self.obj.id)
        field_label = question_model._meta.get_field('draft').verbose_name
        self.assertEquals(field_label, 'Черновик')

    def test_name_max_length(self):
        question_model = models.Question.objects.get(id=self.obj.id)
        max_length = question_model._meta.get_field('name').max_length
        self.assertEquals(max_length, 300)

    def test_type_max_length(self):
        question_model = models.Question.objects.get(id=self.obj.id)
        max_length = question_model._meta.get_field('type').max_length
        self.assertEquals(max_length, 2)

    def test_object_name_is_name(self):
        question_model = models.Question.objects.get(id=self.obj.id)
        expected_object_name = question_model.name
        self.assertEquals(expected_object_name, str(question_model))


class AnswerModelTest(TestCase):
    """Тесты для модели ответов"""

    @classmethod
    def setUpTestData(cls):
        poll = models.Polls.objects.create(name='Тестовый опрос',
                                           from_date=datetime.datetime.strptime(
                                               '04.05.2021', '%d.%m.%Y'),
                                           to_date=datetime.datetime.strptime(
                                               '07.05.2021', '%d.%m.%Y'),
                                           description='тестовое описание')

        question = models.Question.objects.create(polls=poll,
                                                  name='Тестовый вопрос',
                                                  type='1',
                                                  draft=False)

        cls.obj = models.Answer.objects.create(question=question,
                                               text='ответ')

    def test_question_label(self):
        answer_model = models.Answer.objects.get(id=self.obj.id)
        field_label = answer_model._meta.get_field('question').verbose_name
        self.assertEquals(field_label, 'Вопрос')

    def test_text_label(self):
        answer_model = models.Answer.objects.get(id=self.obj.id)
        field_label = answer_model._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Текст ответа')

    def test_text_max_length(self):
        answer_model = models.Answer.objects.get(id=self.obj.id)
        max_length = answer_model._meta.get_field('text').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_text(self):
        answer_model = models.Answer.objects.get(id=self.obj.id)
        expected_object_name = answer_model.text
        self.assertEquals(expected_object_name, str(answer_model))


class UserStatisticModelTest(TestCase):
    """Тесты для модели Статиски по пользователям"""

    @classmethod
    def setUpTestData(cls):
        poll = models.Polls.objects.create(name='Тестовый опрос',
                                           from_date=datetime.datetime.strptime(
                                               '04.05.2021', '%d.%m.%Y'),
                                           to_date=datetime.datetime.strptime(
                                               '07.05.2021', '%d.%m.%Y'),
                                           description='тестовое описание')

        question = models.Question.objects.create(polls=poll,
                                                  name='Тестовый вопрос',
                                                  type='1',
                                                  draft=False)

        answer = models.Answer.objects.create(question=question, text='ответ')
        cls.obj = models.UserStatistic.objects.create(
            user_id=1, question=question, answer=answer.text)

    def test_user_id_label(self):
        model = models.UserStatistic.objects.get(id=self.obj.id)
        field_label = model._meta.get_field('user_id').verbose_name
        self.assertEquals(field_label, 'ID Пользователя')

    def test_question_label(self):
        model = models.UserStatistic.objects.get(id=self.obj.id)
        field_label = model._meta.get_field('question').verbose_name
        self.assertEquals(field_label, 'Вопрос')

    def test_answer_label(self):
        model = models.UserStatistic.objects.get(id=self.obj.id)
        field_label = model._meta.get_field('answer').verbose_name
        self.assertEquals(field_label, 'Текст ответа')

    def test_answer_max_length(self):
        model = models.UserStatistic.objects.get(id=self.obj.id)
        max_length = model._meta.get_field('answer').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_user_id_and_question(self):
        model = models.UserStatistic.objects.get(id=self.obj.id)
        expected_object_name = f'{model.user_id} - {model.question.id}'
        self.assertEquals(expected_object_name, str(model))
