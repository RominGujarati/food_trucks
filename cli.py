import click
from food_truck_finder import FoodTruckFinder

@click.command()
@click.argument('latitude', type=float)
@click.argument('longitude', type=float)
@click.option('--num-trucks', default=5, help='Number of food trucks to return.')
def cli(latitude, longitude, num_trucks):
    finder = FoodTruckFinder('food-truck-data.csv')
    nearest_trucks = finder.find_nearest((latitude, longitude), num_trucks)
    click.echo(nearest_trucks)

if __name__ == "__main__":
    cli()
