from flask import Flask, request, jsonify
from food_truck_finder import FoodTruckFinder

app = Flask(__name__)
finder = FoodTruckFinder('food-truck-data.csv')

@app.route('/api/foodtrucks', methods=['GET'])
def get_food_trucks():
    """
    API endpoint to get the nearest food trucks to a given location.
    
    :return: JSON list of food trucks with details.
    """
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    num_trucks = int(request.args.get('num_trucks', 5))  # Default to 5 if not provided

    # Find the nearest food trucks based on the given coordinates
    nearest_trucks = finder.find_nearest((latitude, longitude), num_trucks)
    return jsonify(nearest_trucks.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
