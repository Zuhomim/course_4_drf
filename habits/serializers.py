from rest_framework import serializers

from habits.models import Habit
from habits.validators import (RelateAndRewardValidator, HabitRelatedHabitIsPleasantValidator, HabitPleasantValidator,
                               CheckHabitValidator, HabitTimeDurationValidator)


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            RelateAndRewardValidator(field1='related_habit', field2='reward'),
            HabitRelatedHabitIsPleasantValidator(field1='related_habit', field2='is_nice'),
            HabitPleasantValidator(field1='related_habit', field2='reward', field3='is_nice'),
            HabitTimeDurationValidator(field='action_time'),
            CheckHabitValidator(field='periodicity')
        ]
