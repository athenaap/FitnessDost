from django.contrib import admin
from .models import UserProfile, Workout, Exercise, FitnessPlan, FitnessGoalQuestionnaire


# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(FitnessPlan)
admin.site.register(FitnessGoalQuestionnaire)
