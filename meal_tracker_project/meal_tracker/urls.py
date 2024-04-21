from django.urls import path
from .views import meal_tracker,bmi_calculator

urlpatterns = [
    path('', meal_tracker, name='meal_tracker'),
    path('bmi-calculator', bmi_calculator, name='bmi-calculator'),

]
