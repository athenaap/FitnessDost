from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Height in meters
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Weight in kilograms

    def __str__(self):
        return self.user.username
    
class Workout(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.user.username}'s Workout on {self.date}"

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class FitnessPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    duration_weeks = models.PositiveIntegerField(default=4)  # Duration of the plan in weeks

    def __str__(self):
        return self.name

class PlanExercise(models.Model):
    plan = models.ForeignKey(FitnessPlan, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    day = models.PositiveIntegerField()  # Day of the plan to perform the exercise
    sets = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['day', 'exercise']

    def __str__(self):
        return f"{self.exercise.name} on day {self.day} of {self.plan.name}"



class UserPlan(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    plan = models.ForeignKey(FitnessPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.user.username}'s Plan: {self.plan.name}"


class FitnessGoalQuestionnaire(models.Model):
    Lose_Weight = 'L'
    Gain_Weight = 'G'
    Gain_Muscle = 'G'
    Other = 'O'
      
    FITNESS_LEVEL_CHOICES = [
        (Lose_Weight, 'Lose Weight'),
        (Gain_Weight, 'Gain Weight'),
        (Gain_Muscle, 'Gain Muscle Mass'),
        (Other, 'Other'),
    ]
      
    goal = models.CharField(
        max_length=2,
        choices=FITNESS_LEVEL_CHOICES,
        default=Lose_Weight,
    )
    age= models.PositiveIntegerField(default=0) 
    height = models.PositiveIntegerField(default=0) 
    weight = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f"Questionnaire for {self.user.username}"