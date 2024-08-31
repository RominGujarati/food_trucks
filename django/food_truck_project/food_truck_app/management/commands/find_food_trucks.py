import pandas as pd
from geopy.distance import geodesic
from django.core.management.base import BaseCommand
from food_truck_finder import FoodTruckFinder

class Command(BaseCommand):
    help = 'Find the nearest food trucks'

    def add_arguments(self, parser):
        parser.add_argument('latitude', type=float, help='Latitude of the location')
        parser.add_argument('longitude', type=float, help='Longitude of the location')
        parser.add_argument('--num-trucks', type=int, default=5, help='Number of food trucks to return')

    def handle(self, *args, **kwargs):
        latitude = kwargs['latitude']
        longitude = kwargs['longitude']
        num_trucks = kwargs['num_trucks']

        finder = FoodTruckFinder('food-truck-data.csv')
        nearest_trucks = finder.find_nearest((latitude, longitude), num_trucks)
        self.stdout.write(str(nearest_trucks))
