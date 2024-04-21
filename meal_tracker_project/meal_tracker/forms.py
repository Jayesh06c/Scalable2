from django import forms

class MealForm(forms.Form):
    meal_name1 = forms.CharField(label='Meal 1')
    grams_consumed1 = forms.IntegerField(label='Grams Consumed for Meal 1', min_value=0)
    meal_name2 = forms.CharField(label='Meal 2')
    grams_consumed2 = forms.IntegerField(label='Grams Consumed for Meal 2', min_value=0)
    meal_name3 = forms.CharField(label='Meal 3')
    grams_consumed3 = forms.IntegerField(label='Grams Consumed for Meal 3', min_value=0)




