from django.urls import path
from .views import FoodTruckView

urlpatterns = [
    path('api/foodtrucks/', FoodTruckView.as_view(), name='food_trucks'),
]
