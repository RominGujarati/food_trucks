from django.http import JsonResponse
from django.views import View
from .food_truck_finder import FoodTruckFinder

class FoodTruckView(View):
    def get(self, request):
        latitude = float(request.GET.get('latitude'))
        longitude = float(request.GET.get('longitude'))
        num_trucks = int(request.GET.get('num_trucks', 5))  # Default to 5 if not provided

        # Instantiate the finder and get the nearest food trucks
        finder = FoodTruckFinder('food-truck-data.csv')
        nearest_trucks = finder.find_nearest((latitude, longitude), num_trucks)
        
        return JsonResponse(nearest_trucks.to_dict(orient='records'), safe=False)
