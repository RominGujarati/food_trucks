import pandas as pd
from geopy.distance import geodesic

class FoodTruckFinder:
    def __init__(self, csv_file='Mobile_Food_Facility_Permit.csv'):
        self.df = pd.read_csv(csv_file)
        
        # Drop rows where 'Latitude' or 'Longitude' are missing
        self.df = self.df.dropna(subset=['Latitude', 'Longitude'])
        
        # Filter the DataFrame to only include food trucks with 'APPROVED' status
        self.df = self.df[self.df['Status'] == 'APPROVED']
    
    def find_nearest(self, user_location, num_trucks=5):
        """
        Finds the nearest food trucks to the user's location.
        
        :param user_location: Tuple containing (latitude, longitude) of the user's location.
        :param num_trucks: Number of food trucks to return (default is 5).
        :return: A DataFrame containing the nearest food trucks.
        """
        
        # Calculate the distance from the user's location to each food truck
        self.df['Distance'] = self.df.apply(
            lambda row: geodesic(user_location, (row['Latitude'], row['Longitude'])).miles,
            axis=1
        )
        nearest_trucks = self.df.sort_values('Distance').head(num_trucks)
        return nearest_trucks[['Applicant', 'Address', 'FoodItems', 'Distance']]

# Example usage (this runs if the script is executed directly):
if __name__ == "__main__":
    finder = FoodTruckFinder('Mobile_Food_Facility_Permit.csv')
    location = (37.7749, -122.4194)  # Example: San Francisco city center
    nearest_trucks = finder.find_nearest(location)
    print(nearest_trucks)
