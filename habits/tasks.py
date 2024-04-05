from datetime import datetime, date, timedelta

import requests
from celery import shared_task
from django.conf import settings

from habits.models import Habit


@shared_task
def send_habit_reminder():
    """
    Отправка напоминания о привычке в телеграм
    """

    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    date_now = date.today()
    time_now = datetime.now().time().replace(second=0, microsecond=0)
    habits_to_send = Habit.objects.filter(is_nice=False)

    for habit in habits_to_send:
        if habit.date == date_now or not habit.date:
            if habit.time >= time_now:
                chat_id = habit.user.telegram_id
                text = f"Вам нужно {habit.action} в {habit.place} в {habit.date_time}"
                requests.post(
                    url=f"{URL}{TOKEN}/sendMessage",
                    data={
                        "chat_id": chat_id,
                        "text": text
                    }
                )
            habit.date_time = date_now + timedelta(days=habit.periodicity)
            habit.save()
