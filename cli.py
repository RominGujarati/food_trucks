import click
from food_truck_finder import FoodTruckFinder

@click.command()
@click.argument('latitude', type=float)
@click.argument('longitude', type=float)
@click.option('--num-trucks', default=5, help='Number of food trucks to return.')
def cli(latitude, longitude, num_trucks):
    """
    Command-line interface for finding the nearest food trucks.
    
    :param latitude: Latitude of the user's location.
    :param longitude: Longitude of the user's location.
    :param num_trucks: Number of food trucks to return (default is 5).
    """
    finder = FoodTruckFinder('food-truck-data.csv')
    
    # Find the nearest food trucks based on the given coordinates
    nearest_trucks = finder.find_nearest((latitude, longitude), num_trucks)
    click.echo(nearest_trucks)

if __name__ == "__main__":
    cli()
