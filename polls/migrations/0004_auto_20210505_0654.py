# Generated by Django 2.2.10 on 2021-05-05 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0003_auto_20210505_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='polls',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions',
                                    to='polls.Polls', verbose_name='Опрос'),
        ),
        migrations.AlterField(
            model_name='userstatistic',
            name='answer',
            field=models.CharField(
                max_length=200, verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='userstatistic',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_user',
                                    to='polls.Question', verbose_name='Вопрос'),
        ),
    ]
