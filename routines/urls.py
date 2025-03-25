from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView,
    ExerciseViewSet,
    RoutineViewSet,
    RoutineExerciseViewSet,
)

router = DefaultRouter()
router.register(r"exercises", ExerciseViewSet, basename="exercises")
router.register(r"routines", RoutineViewSet, basename="routines")
router.register(r"routine-exercises", RoutineExerciseViewSet, basename="routine-exercise")


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]

urlpatterns += router.urls