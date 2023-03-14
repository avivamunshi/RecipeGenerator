"""This module contains functions for finding recipes based on a list of ingredients."""
import os
import csv
import json
import random
from recipe_scrapers import scrape_me #pylint: disable=import-error

recipe_json_list = []

# get the absolute path of the directory containing this script
function_dir = os.path.dirname(os.path.abspath(__file__))

# construct the path to the CSV file using the script directory as the base path
csv_path = os.path.join(function_dir, '../code/web_links.csv')

# check if the CSV file exists before proceeding
if os.path.exists(csv_path):
    with open(csv_path, encoding='utf-8') as file:
        reader = csv.reader(file)
        recipe_json_list = []
        for row in reader:
            url = row[0]
            scraper = scrape_me(url, wild_mode=True)
            recipe_json_list.append(scraper.to_json())
else:
    print("Error: Could not find web_links.csv file.")

with open('recipe_json_list.txt', 'w', encoding='utf-8') as file:
    json.dump(recipe_json_list, file)

def find_recipe(ingredients, refresh=False):

    """
    Find a recipe that includes all the specified ingredients.

    Args:
        ingredients (str): A comma-separated string of ingredients.
        refresh (bool, optional): Whether to randomly shuffle the recipe list. Defaults to False.

    Returns:
        dict or None: A dictionary representing the matching recipe or None if no recipe was found.

    Further the try-except block raises:
    FileNotFoundError: If the recipe data file cannot be found.
j   son.JSONDecodeError: If the recipe data file cannot be decoded.
    """

    # get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # construct the path to the JSON file using the script directory as the base path
    json_path = os.path.join(script_dir, 'recipe_json_list.txt')

    try:
        with open(json_path, 'r', encoding='utf-8') as f_1:
            recipe_data = json.load(f_1)
    except FileNotFoundError:
        print("The recipe data file could not be found.")
        recipe_data = None
    except json.JSONDecodeError:
        print("The recipe data file could not be decoded.")
        recipe_data = None

    if refresh:
        random.shuffle(recipe_data)

    ingredients_list = [i.strip().lower() for i in ingredients.split(',')]
    matching_recipes = []

    for recipe in recipe_data:
        recipe_ingredients = [ingredient.lower() for ingredient in recipe['ingredients']]
        flag = 0

        for i in ingredients_list:
            for j in recipe_ingredients:
                if i in j:
                    flag += 1
                    break
            if flag == len(ingredients_list):
                matching_recipes.append(recipe)
                break

    if not matching_recipes:
        return None
    return random.choice(matching_recipes)

print(find_recipe('milk, eggs'))
