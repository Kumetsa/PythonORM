import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import ArtworkGallery, ChessPlayer, Meal, Dungeon, Workout
from django.db.models import Case, When, Value, F


# Task 1

# def show_highest_rated_art() -> str:
#     best_artwork =  ArtworkGallery.objects.order_by('-rating', 'id').first()
#
#     return f"{best_artwork.art_name} is the highest-rated art with a {best_artwork.rating} rating!"
#
#
# def bulk_create_arts(first_art, second_art) -> None:
#     ArtworkGallery.objects.bulk_create(
#         [
#             first_art,
#             second_art
#         ]
#     )
#
#
# def delete_negative_rated_arts():
#     ArtworkGallery.objects.filter(rating__lte=0).delete()
#
# artwork1 = ArtworkGallery(artist_name="Vincent van Gogh", art_name="Starry Night", rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name="Leonardo da Vinci", art_name="Mona Lisa", rating=5, price=1500000.0)
#
# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())

# Task 2

# from main_app.models import Laptop
#
#
# def show_the_most_expensive_laptop():
#     most_expensive_laptop = Laptop.objects.order_by('-price', '-id').first()
#
#     return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"
#
#
# def bulk_create_laptops(args):
#     Laptop.objects.bulk_create(args)
#
#
# def update_to_512_GB_storage():
#     Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)
#
#
# def update_to_16_GB_memory():
#     Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)
#
#
# def update_operation_systems():
#     Laptop.objects.filter(brand="Asus").update(operation_system="Windows")
#     Laptop.objects.filter(brand="Apple").update(operation_system="MacOS")
#     Laptop.objects.filter(brand__in=["Dell", "Acer"]).update(operation_system="Linux")
#     Laptop.objects.filter(brand="Lenovo").update(operation_system="Chrome OS")
#
#
# def delete_inexpensive_laptops():
#     Laptop.objects.filter(price__lt=1200).delete()

# # Create three instances of Laptop
# laptop1 = Laptop(
#     brand='Asus',
#     processor='Intel Core i5',
#     memory=8,
#     storage=256,
#     operation_system='Windows',
#     price=899.99
# )
#
# laptop2 = Laptop(
#     brand='Apple',
#     processor='Apple M1',
#     memory=16,
#     storage=512,
#     operation_system='MacOS',
#     price=1399.99
#
# )
#
# laptop3 = Laptop(
#     brand='Lenovo',
#     processor='AMD Ryzen 7',
#     memory=12,
#     storage=512,
#     operation_system='Linux',
#     price=999.99,
# )
#
# # Create a list of instances
# laptops_to_create = [laptop1, laptop2, laptop3]
#
# # Use bulk_create to save the instances
# bulk_create_laptops(laptops_to_create)
#
# # Execute the following functions
# update_to_512_GB_storage()
# update_operation_systems()
#
# # Retrieve 2 laptops from the database
# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
#
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)


# Task 3

# def bulk_create_chess_players(args):
#     ChessPlayer.objects.bulk_create(args)
#
# def delete_chess_players():
#     ChessPlayer.objects.filter(title='no title').delete()
#
# def change_chess_games_won():
#     ChessPlayer.objects.filter(title='GM').update(games_won=30)
#
# def change_chess_games_lost():
#     ChessPlayer.objects.filter(title='no title').update(games_lost=25)
#
# def change_chess_games_drawn():
#     ChessPlayer.objects.update(games_drawn=10)
#
# def grand_chess_title_GM():
#     ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')
#
# def grand_chess_title_IM():
#     ChessPlayer.objects.filter(rating__lte=2399, rating__gte=2300).update(title='IM')
#
# def grand_chess_title_FM():
#     ChessPlayer.objects.filter(rating__lte=2299, rating__gte=2200).update(title='FM')
#
# def grand_chess_title_regular_player():
#     ChessPlayer.objects.filter(rating__lte=2199, rating__gte=0).update(title='regular player')

# # Create two instances of ChessPlayer
# player1 = ChessPlayer(
#     username='Player1',
#     title='no title',
#     rating=2200,
#     games_played=50,
#     games_won=20,
#     games_lost=25,
#     games_drawn=5,
# )
# player2 = ChessPlayer(
#     username='Player2',
#     title='IM',
#     rating=2350,
#     games_played=80,
#     games_won=40,
#     games_lost=25,
#     games_drawn=15,
# )
#
# # Call the bulk_create_chess_players function
# bulk_create_chess_players([player1, player2])
#
# # Call the delete_chess_players function
# delete_chess_players()
#
# # Check that the players are deleted
# print("Number of Chess Players after deletion:", ChessPlayer.objects.count())


# Task 4

# def set_new_chefs():
#     Meal.objects.update(
#         chef=Case(
#             When(meal_type='Breakfast', then=Value('Gordon Ramsay')),
#             When(meal_type='Lunch', then=Value('Julia Child')),
#             When(meal_type='Dinner', then=Value('Jamie Oliver')),
#             When(meal_type='Snack', then=Value('Thomas Keller')),
#             default=F('chef')
#         )
#     )
#
#
# def set_new_preparation_times():
#     Meal.objects.update(
#         preparation_time=Case(
#             When(meal_type='Breakfast', then=Value('10 minutes')),
#             When(meal_type='Lunch', then=Value('12 minutes')),
#             When(meal_type='Dinner', then=Value('15 minutes')),
#             When(meal_type='Snack', then=Value('5 minutes')),
#             default=F('preparation_time')
#         )
#     )
#
#
# def update_low_calorie_meals():
#     Meal.objects.filter(meal_type__in=["Breakfast","Dinner"]).update(calories=400)
#
#
# def update_high_calorie_meals():
#     Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).update(calories=700)
#
#
# def delete_lunch_and_snack_meals():
#     Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).delete()


# # Create two instances of the Meal model
# meal1 = Meal.objects.create(
#     name="Pancakes",
#     meal_type="Breakfast",
#     preparation_time="20 minutes",
#     difficulty=3,
#     calories=350,
#     chef="Jane",
# )
#
# meal2 = Meal.objects.create(
#     name="Spaghetti Bolognese",
#     meal_type="Dinner",
#     preparation_time="45 minutes",
#     difficulty=4,
#     calories=550,
#     chef="Sarah",
# )
# # Test the set_new_chefs function
# set_new_chefs()
#
# # Test the set_new_preparation_times function
# set_new_preparation_times()
#
# # Refreshes the instances
# meal1.refresh_from_db()
# meal2.refresh_from_db()
#
# # Print the updated meal information
# print("Meal 1 Chef:", meal1.chef)
# print("Meal 1 Preparation Time:", meal1.preparation_time)
# print("Meal 2 Chef:", meal2.chef)
# print("Meal 2 Preparation Time:", meal2.preparation_time)


# Task 5

# def show_hard_dungeons():
#     hard_dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')
#
#     result = []
#
#     for dungeon in hard_dungeons:
#         result.append(
#             f"{dungeon.name} is guarded by {dungeon.boss_name} "
#             f"who has {dungeon.boss_health} health points!"
#         )
#
#     return '\n'.join(result)
#
#
# def bulk_create_dungeons(*args):
#     Dungeon.objects.bulk_create(*args)
#
#
# def update_dungeon_names() -> None:
#     Dungeon.objects.filter(difficulty="Easy").update(name="The Erased Thombs")
#     Dungeon.objects.filter(difficulty="Medium").update(name="The Coral Labyrinth")
#     Dungeon.objects.filter(difficulty="Hard").update(name="The Lost Haunt")
#
#
# def update_dungeon_bosses_health() -> None:
#     Dungeon.objects.exclude(difficulty="Easy").update(boss_health=500)
#
#
# def update_dungeon_recommended_levels() -> None:
#     Dungeon.objects.filter(difficulty="Easy").update(recommended_level=25)
#     Dungeon.objects.filter(difficulty="Medium").update(recommended_level=50)
#     Dungeon.objects.filter(difficulty="Hard").update(recommended_level=75)
#
#
# def update_dungeon_rewards() -> None:
#     Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
#     Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
#     Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")
#
#
# def set_new_locations() -> None:
#     Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
#     Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
#     Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")


# # Create two instances
# dungeon1 = Dungeon(
#     name="Dungeon 1",
#     boss_name="Boss 1",
#     boss_health=1000,
#     recommended_level=75,
#     reward="Gold",
#     location="Eternal Hell",
#     difficulty="Hard",
# )
#
# dungeon2 = Dungeon(
#     name="Dungeon 2",
#     boss_name="Boss 2",
#     boss_health=500,
#     recommended_level=25,
#     reward="Experience",
#     location="Crystal Caverns",
#     difficulty="Easy",
# )

# # Bulk save the instances
# bulk_create_dungeons([dungeon1, dungeon2])
#
# # Update boss's health
# update_dungeon_bosses_health()
#
# # Show hard dungeons
# hard_dungeons_info = show_hard_dungeons()
# print(hard_dungeons_info)
#
# # Change dungeon names based on difficulty
# update_dungeon_names()
# dungeons = Dungeon.objects.all()
# print(dungeons[0].name)
# print(dungeons[1].name)
#
# # Change the dungeon rewards
# update_dungeon_rewards()
# dungeons = Dungeon.objects.all()
# print(dungeons[0].reward)
# print(dungeons[1].reward)


#Task 6


# def show_workouts():
#     workouts = Workout.objects.filter(workout_type__in=["Calisthenics", "CrossFit"])
#
#     result = [f"{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!"
#               for workout in workouts]
#
#     return '\n'.join(result)
#
#
# def get_high_difficulty_cardio_workouts():
#     return Workout.objects.filter(workout_type="Cardio", difficulty="High").order_by('instructor')
#
#
# def set_new_instructors():
#     Workout.objects.update(
#         instructor=Case(
#             When(workout_type="Cardio", then=Value("John Smith")),
#             When(workout_type="Strength", then=Value("Michael Williams")),
#             When(workout_type="Yoga", then=Value("Emily Johnson")),
#             When(workout_type="CrossFit", then=Value("Sarah Davis")),
#             When(workout_type="Calisthenics", then=Value("Chris Heria")),
#             default=F('instructor'),
#         )
#     )
#
#
# def set_new_duration_times():
#     Workout.objects.update(
#         duration=Case(
#             When(instructor="John Smith", then=Value("15 minutes")),
#             When(instructor="Sarah Davis", then=Value("30 minutes")),
#             When(instructor="Chris Heria", then=Value("45 minutes")),
#             When(instructor="Michael Williams", then=Value("1 hour")),
#             When(instructor="Emily Johnson", then=Value("1 hour and 30 minutes")),
#             default=F('duration'),
#         )
#     )
#
#
# def delete_workouts():
#     Workout.objects.exclude(workout_type__in=["Strength", "Calisthenics"]).delete()


# # Create two Workout instances
# workout1 = Workout.objects.create(
#     name="Push-Ups",
#     workout_type="Calisthenics",
#     duration="10 minutes",
#     difficulty="Intermediate",
#     calories_burned=200,
#     instructor="Chris Heria"
# )
#
# workout2 = Workout.objects.create(
#     name="Running",
#     workout_type="Cardio",
#     duration="30 minutes",
#     difficulty="High",
#     calories_burned=400,
#     instructor="John Smith"
# )
#
# # Run the functions
# print(show_workouts())
#
# high_difficulty_cardio_workouts = get_high_difficulty_cardio_workouts()
#
# for workout in high_difficulty_cardio_workouts:
#     print(f"{workout.name} by {workout.instructor}")
#
# set_new_instructors()
# workouts_with_new_instructors = Workout.objects.all()
# for workout in workouts_with_new_instructors:
#     print(f"Instructor: {workout.instructor}")
#
# set_new_duration_times()
# workouts_with_new_durations = Workout.objects.all()
# for workout in workouts_with_new_durations:
#     print(f"Duration: {workout.duration}")
