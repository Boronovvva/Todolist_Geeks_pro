# Generated by Django 5.0.6 on 2024-07-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название задания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('completed', models.BooleanField(default=False, verbose_name='Статус выполнения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата задания')),
            ],
            options={
                'verbose_name': 'Список задач',
                'verbose_name_plural': 'Списки задач',
            },
        ),
    ]
