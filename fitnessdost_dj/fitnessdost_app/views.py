from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import UserProfile, FitnessGoalQuestionnaire
from .forms import FitnessGoalQuestionnaireForm

def home(requests):
     return render(requests, 'home.html')


def user_profile(request, user_id):
    profile = get_object_or_404(UserProfile, user__id=user_id)
    return render(request, 'user_profile.html', {'profile': profile})


def questionnaire_view(request):
    if request.method == 'POST':
        form = FitnessGoalQuestionnaireForm(request.POST)
        if form.is_valid():
            questionnaire = form.save(commit=False)
            questionnaire.user = request.user
            questionnaire.save()
            return redirect('/home')  # Redirect to home after submission
    else:
        form = FitnessGoalQuestionnaireForm()

    return render(request, 'questionnaire.html', {'form': form})