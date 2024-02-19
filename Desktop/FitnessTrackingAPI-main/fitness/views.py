from django.db.models import Sum
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from rest_framework import viewsets, permissions
from .models import Workout, Exercise, FitnessData
from .serializers import WorkoutSerializer, ExerciseSerializer, FitnessDataSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)
    
    
class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FitnessDataViewSet(viewsets.ModelViewSet):
    serializer_class = FitnessDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FitnessData.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutAnalytics(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request):
        workouts = Workout.objects.filter(user=request.user)
        calories = workouts.aggregate(Sum('calories_burned'))
        workouts = workouts.count()
        return JsonResponse({'workouts': workouts, 'calories': calories['calories_burned__sum']}, safe=False)
