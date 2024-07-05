from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    title = models.CharField(
        max_length = 100,
        verbose_name='Название задания',
        unique=True
    )

    description = models.TextField(
        verbose_name = 'Описание'
    )

    completed = models.BooleanField(
        default=False,
        verbose_name = 'Статус выполнения'
    )

    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата задания'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Списки задач'