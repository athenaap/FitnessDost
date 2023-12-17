
from django.urls import include, path
from . import views
from .views import home

from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.home, name='home'),
        path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
        path('questionnaire/', views.questionnaire_view, name='questionnaire'),
] 