# food_truck_app/food_truck_finder.py

import pandas as pd
from geopy.distance import geodesic
import os

class FoodTruckFinder:
    def __init__(self, csv_file='food-truck-data.csv'):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, csv_file)
        self.df = pd.read_csv(csv_path)
        self.df = self.df.dropna(subset=['Latitude', 'Longitude'])
        self.df = self.df[self.df['Status'] == 'APPROVED']

    def find_nearest(self, user_location, num_trucks=5):
        self.df['Distance'] = self.df.apply(
            lambda row: geodesic(user_location, (row['Latitude'], row['Longitude'])).miles,
            axis=1
        )
        nearest_trucks = self.df.sort_values('Distance').head(num_trucks)
        return nearest_trucks[['Applicant', 'Address', 'FoodItems', 'Distance']]
