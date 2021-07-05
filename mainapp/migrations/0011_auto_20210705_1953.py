# Generated by Django 3.2.4 on 2021-07-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_comment_is_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='answer',
            field=models.CharField(blank=True, default='Now answer', max_length=500, verbose_name='Ответ'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11')], default=None, null=True, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Рисунок к условию'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, default='No title', max_length=100, verbose_name='Название задачи'),
            preserve_default=False,
        ),
    ]