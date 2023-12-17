from django import forms
from .models import FitnessGoalQuestionnaire

class FitnessGoalQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = FitnessGoalQuestionnaire
        fields = '__all__'