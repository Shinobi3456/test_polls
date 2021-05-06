from django.db import models


class Polls(models.Model):
    """Опросы"""

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    name = models.CharField("Название", max_length=250)
    from_date = models.DateField("Дата старта")
    to_date = models.DateField("Дата окончания")
    description = models.TextField("Описание", max_length=500)

    def __str__(self):
        return f'{self.name} {self.from_date.strftime("%d.%m.%Y")}-{self.to_date.strftime("%d.%m.%Y")}'


class Question(models.Model):
    """Вопросы для опроса"""

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    TYPE_CHOICES = (
        ('0', 'ответ текстом'),
        ('1', 'ответ с выбором одного варианта'),
        ('2', 'ответ с выбором нескольких вариантов'),
    )
    polls = models.ForeignKey(
        Polls, on_delete=models.CASCADE, verbose_name="Опрос", related_name='questions')
    name = models.CharField("Текст вопроса", max_length=300)
    type = models.CharField(
        "Тип вопроса", choices=TYPE_CHOICES, default='1', max_length=2)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name


class Answer(models.Model):
    """Варианты ответов"""

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'

    question = models.ForeignKey(
        Question, verbose_name="Вопрос", on_delete=models.CASCADE, related_name='options')
    text = models.CharField("Текст ответа", max_length=200)

    def __str__(self):
        return self.text


class UserStatistic(models.Model):
    """Статистика ответов пользователя"""

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    user_id = models.PositiveIntegerField("ID Пользователя")
    question = models.ForeignKey(
        Question, verbose_name="Вопрос", on_delete=models.CASCADE, related_name='answer_user')
    answer = models.CharField("Текст ответа", max_length=200)

    def __str__(self):
        return f'{self.user_id} - {self.question.id}'
