from django.urls import path,include
from .views import WorkoutViewSet,ExerciseViewSet, FitnessDataViewSet, WorkoutAnalytics
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'fitnessdata', FitnessDataViewSet,basename='fitnessdata')
router.register(r'workouts', WorkoutViewSet,basename='workouts')
router.register(r'exercises', ExerciseViewSet,basename='exercises')

urlpatterns = [
    path('', include(router.urls)),
    path('workoutanalytics/', WorkoutAnalytics.as_view(), name='workoutanalytics'),
]   