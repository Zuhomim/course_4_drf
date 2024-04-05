from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь")
    place = models.CharField(max_length=100, verbose_name="место")
    date = models.DateField(verbose_name="дата", **NULLABLE)
    date_time = models.TimeField(default="10:00:00", verbose_name="время", **NULLABLE)
    action = models.CharField(max_length=100, verbose_name="действие")
    is_nice = models.BooleanField(default=False, verbose_name="признак приятной привычки")
    related_habit = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="связанная привычка", **NULLABLE)
    periodicity = models.SmallIntegerField(default=1, verbose_name="периодичность", **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name="вознаграждение", **NULLABLE)
    action_time = models.IntegerField(verbose_name="время выполнения")
    is_public = models.BooleanField(default=False, verbose_name="признак публичности")

    def __str__(self):
        return f'{self.user} будет {self.action} в {self.date_time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
