import pandas as pd
from geopy.distance import geodesic

class FoodTruckFinder:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

    def find_nearest(self, user_location, num_trucks=5):
        self.df['Distance'] = self.df.apply(
            lambda row: geodesic(user_location, (row['Latitude'], row['Longitude'])).miles,
            axis=1
        )
        nearest_trucks = self.df.sort_values('Distance').head(num_trucks)
        return nearest_trucks[['Applicant', 'Address', 'FoodItems', 'Distance']]

# Example usage in CLI
if __name__ == "__main__":
    finder = FoodTruckFinder('food-truck-data.csv')
    location = (37.7749, -122.4194)
    nearest_trucks = finder.find_nearest(location)
    print(nearest_trucks)
