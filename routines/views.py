from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Exercise, Routine, RoutineExercise
from .serializers import (
    UserSerializer, ExerciseSerializer,
    RoutineSerializer, RoutineExerciseSerializer,
)
from rest_framework.decorators import action
from rest_framework import status


# Registro de usuario
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# CRUD ejercicios
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

# CRUD rutinas
class RoutineViewSet(viewsets.ModelViewSet):
    serializer_class = RoutineSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Routine.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'], url_path='by-user/(?P<user_id>[^/.]+)')
    def by_user(self, request, user_id=None):
        routines = Routine.objects.filter(user__id=user_id)
        serializer = self.get_serializer(routines, many=True)
        return Response(serializer.data)

# Relación rutina-ejercicio
class RoutineExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = RoutineExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RoutineExercise.objects.filter(routine__user=self.request.user)