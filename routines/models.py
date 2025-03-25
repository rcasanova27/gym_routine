from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=20)  # Lunes, Martes, etc.
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.day} @ {self.time}"

class RoutineExercise(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='routine_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.routine.name} → {self.exercise.name}"