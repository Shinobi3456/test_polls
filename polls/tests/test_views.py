import datetime
from collections import OrderedDict

from django.test import TestCase
from django.urls import reverse

from polls.models import Polls


class PollsListTest(TestCase):
    """Тестирование списка опросов"""
    polls_index = reverse('polls_view')

    def setUp(self):
        current_date = datetime.datetime.today()

        self.actual_polls = Polls.objects.create(name='Актуальный опрос',
                                                 from_date=current_date,
                                                 to_date=current_date + datetime.timedelta(days=5))
        Polls.objects.create(name='Прошлый опрос',
                             from_date=current_date -
                             datetime.timedelta(days=10),
                             to_date=current_date - datetime.timedelta(days=5))

    def test_get_index_success(self):
        """Проверка успешного получения данных опроса"""
        resp = self.client.get(self.polls_index)
        data_out = [OrderedDict([('id', self.actual_polls.id), ('name', self.actual_polls.name),
                                 ('from_date', self.actual_polls.from_date.strftime(
                                     '%Y-%m-%d')),
                                 ('to_date', self.actual_polls.to_date.strftime(
                                     '%Y-%m-%d')),
                                 ('description', self.actual_polls.description)])]

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, data_out)

    def tearDown(self):
        Polls.objects.all().delete()


class PollsDetailTest(TestCase):
    fixtures = ['polls', 'question', 'answer']
    polls_detail = reverse('question_view', kwargs={'polls_id': 1})

    def test_get_detail_success(self):
        """Проверка успешного получения списка вопросов"""
        resp = self.client.get(self.polls_detail)
        data_out = [OrderedDict([('id', 1), ('name', 'Тестовый вопрос'), ('type', '0'), ('options', [])]),
                    OrderedDict([('id', 2), ('name', 'Тестовый вопрос 1'), ('type', '1'),
                                 ('options', [OrderedDict([('id', 1), ('text', 'ответ 1')])])]),
                    OrderedDict([('id', 3), ('name', 'Тестовый вопрос 2'), ('type', '2'),
                                 ('options', [OrderedDict([('id', 2), ('text', 'ответ 2')]),
                                              OrderedDict([('id', 3), ('text', 'ответ 3')])])])]

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, data_out)


class AnswerSaveViewTest(TestCase):
    fixtures = ['polls', 'question', 'answer']
    answer_save = reverse('answer_save_view')

    def test_answer_save_success(self):
        """Проверка успешного сохранения ответа на вопрос"""
        resp = self.client.post(self.answer_save,
                                data={'user_id': 1, 'question': 1, 'answer': 'тект тест'})
        self.assertEqual(resp.status_code, 200)

    def test_answer_save_use_get(self):
        """Негативная проверка на попытку послать данные через GET"""
        resp = self.client.get(self.answer_save,
                               data={'user_id': 1, 'question': 1, 'answer': 'тект тест'})
        self.assertEqual(resp.status_code, 405)


class StatisticUserViewTest(TestCase):
    fixtures = ['polls', 'question', 'answer', 'user_statistic']
    statistic_user = reverse('statistic_view', kwargs={'user_id': 1})

    def test_get_statistic_user(self):
        """Получения статистики опросов по пользователю"""
        resp = self.client.get(self.statistic_user)
        print(resp.data)
        data_out = [OrderedDict([('id', 3), ('name', 'Тестовый опрос 2'), ('from_date', '2021-05-05'),
                                 ('to_date', '2021-05-09'), ('description',
                                                             'Тестовый опрос 2'),
                                 ('questions', [OrderedDict([('id', 4), ('name', 'Тестовый вопрос 3'),
                                                             ('type', '0'),
                                                             ('answer_user',
                                                              [OrderedDict([('id', 1),
                                                                            ('answer', 'произвольный ответ')])])]),
                                                OrderedDict([('id', 5), ('name', 'Тестовый вопрос 4'), ('type', '1'),
                                                             ('answer_user', [])]),
                                                OrderedDict([('id', 6), ('name', 'Тестовый вопрос 5'),
                                                             ('type', '2'), ('answer_user', [])])])])]
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, data_out)
