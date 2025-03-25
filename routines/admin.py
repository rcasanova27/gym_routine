from django.contrib import admin
from .models import Routine, Exercise, RoutineExercise

admin.site.register(Routine)
admin.site.register(Exercise)
admin.site.register(RoutineExercise)