from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@gmail.com",
            is_staff=True,
            is_active=True,
            is_superuser=False
        )
        self.user.set_password('test_pass')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place='test_place',
            action='test_action',
            user=self.user,
            action_time=100
        )

    def test_create_habit(self):
        """Тест создания привычки"""

        data = {
            'place': 'test_place',
            'action': 'test_action',
            'user': self.user.pk,
            'action_time': 100
        }

        response = self.client.post('/habits/create/', data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Habit.objects.all().count(), 2)

    def test_list_habit(self):
        """Тест вывода списка привычек"""

        response = self.client.get('/habits/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.habit.id,
                            'place': 'test_place',
                            'date_time': self.habit.date_time,
                            'date': self.habit.date,
                            'action': 'test_action',
                            'is_nice': self.habit.is_nice,
                            'reward': self.habit.reward,
                            'action_time': self.habit.action_time,
                            'periodicity': self.habit.periodicity,
                            'is_public': self.habit.is_public,
                            'user': self.user.pk,
                            'related_habit': self.habit.related_habit
                        }
                    ]
            }
        )

    def test_update_habit(self):
        """Тестирование изменения привычки"""

        change_data = {
            'place': 'place_changed',
            'action': 'action_changed'
        }
        response = self.client.patch(f'/habits/update/{self.habit.id}/', data=change_data)
        self.maxDiff = None

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {
                'id': self.habit.id,
                'place': 'place_changed',
                'date_time': self.habit.date_time,
                'date': self.habit.date,
                'action': 'action_changed',
                'is_nice': self.habit.is_nice,
                'reward': self.habit.reward,
                'action_time': self.habit.action_time,
                'periodicity': self.habit.periodicity,
                'is_public': self.habit.is_public,
                'user': self.user.pk,
                'related_habit': self.habit.related_habit
            }
        )

    def test_duration_habit(self):
        """Тест создания привычки со временем исполнения более 2 минут"""

        data = {
            'place': 'test_place',
            'action': 'test_action',
            'action_time': '150',
            'user': self.user.pk,
        }
        response = self.client.post('/habits/create/', data=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_periodicity_habit(self):
        """Тест создания привычки с периодичностью менее 1 раза в неделю (periodicity > 7)"""

        data = {
            'place': 'test_place',
            'action': 'test_action',
            'periodicity': 8,
            'user': self.user.pk,
            'action_time': 100
        }
        response = self.client.post('/habits/create/', data=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reward_and_pleasant_habit(self):
        """Тест создания привычки с наградой и приятной привычкой одновременно"""

        data = {
            'place': 'test_place',
            'action': 'test_action',
            'reward': 'test_reward',
            'user': self.user.pk,
            'related_habit': 1,
            'action_time': 100
        }
        response = self.client.post('/habits/create/', data=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)