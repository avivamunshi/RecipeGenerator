"""This module contains functions for finding recipes based on a list of ingredients."""
import csv
import json
import random
from recipe_scrapers import scrape_me

recipe_json_list = []

with open('/Users/aviva/Documents/RecipeGenerator/web_links.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        url = row[0]
        scraper = scrape_me(url, wild_mode=True)
        recipe_json_list.append(scraper.to_json())

with open('recipe_json_list.txt', 'w') as file:
    #this has now been written to original_recipe_json_list.txt
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

    try:
        with open('/Users/aviva/Documents/RecipeGenerator/original_recipe_json_list.txt','r')as f_1:
            recipe_data = json.load(f_1)
    except FileNotFoundError:
        print("The recipe data file could not be found.")
        return None
    except json.JSONDecodeError:
        print("The recipe data file could not be decoded.")
        return None

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
