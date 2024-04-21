import requests
from django.shortcuts import render
from .forms import MealForm

def meal_tracker(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal_name1 = form.cleaned_data['meal_name1']
            grams_consumed1 = form.cleaned_data['grams_consumed1']
            meal_name2 = form.cleaned_data['meal_name2']
            grams_consumed2 = form.cleaned_data['grams_consumed2']
            meal_name3 = form.cleaned_data['meal_name3']
            grams_consumed3 = form.cleaned_data['grams_consumed3']

            meal_details = []

            # Calculate total grams consumed
            total_grams = grams_consumed1 + grams_consumed2 + grams_consumed3

            # Process each meal to get nutritional information
            for meal_name, grams_consumed in [(meal_name1, grams_consumed1), (meal_name2, grams_consumed2), (meal_name3, grams_consumed3)]:
                query = f"{grams_consumed} gram {meal_name}"
                YOUR_API_KEY = "nKIDW5Xq3Fag7BaoDaqRVg==JwVLb1fVXFclI4k8"
                api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
                response = requests.get(api_url, headers={'X-Api-Key': YOUR_API_KEY})

                if response.status_code == requests.codes.ok:
                    data = response.json()
                    meal = data[0]
                    meal_details.append({
                        'name': meal_name,
                        'grams_consumed': grams_consumed,
                        'calories': meal['calories'],
                        'fat_total_g': meal['fat_total_g'],
                        'fat_saturated_g': meal['fat_saturated_g'],
                        'protein_g': meal['protein_g'],
                        'sodium_mg': meal['sodium_mg'],
                        'potassium_mg': meal['potassium_mg'],
                        'cholesterol_mg': meal['cholesterol_mg'],
                        'carbohydrates_total_g': meal['carbohydrates_total_g'],
                        'fiber_g': meal['fiber_g'],
                        'sugar_g': meal['sugar_g']
                    })
        
            return render(request, 'meal_tracker/thanks.html', {'total_grams': total_grams, 'meal_details': meal_details})
    else:
        form = MealForm()
    return render(request, 'meal_tracker/meal_tracker.html', {'form': form})

def bmi_calculator(request):
    if request.method == 'POST':
        height = int(request.POST.get('height'))
        weight = int(request.POST.get('weight'))
        print("IEIGHT",height,weight)
        response = requests.post('https://0zgcydxjzg.execute-api.eu-west-1.amazonaws.com/STAGE/testing', json = {'height': height, 'weight': weight})
        print(response.text)
        return render(request, 'bm_calculator.html', {'bmi_result': response.json(), 'error': None})
    return render(request, 'bm_calculator.html', {'bmi_result': None, 'error': None})
