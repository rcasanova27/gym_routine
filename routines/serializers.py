from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Exercise, Routine, RoutineExercise

# Usuario (para registro o consulta)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Ejercicio
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

# Relación rutina-ejercicio
class RoutineExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.ReadOnlyField(source="exercise.name")

    class Meta:
        model = RoutineExercise
        fields = ["id", "exercise", "exercise_name"]

# Rutina
class RoutineSerializer(serializers.ModelSerializer):
    routine_exercises = RoutineExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Routine
        fields = ["id", "name", "day", "time", "user", "routine_exercises"]
        read_only_fields = ["user"]