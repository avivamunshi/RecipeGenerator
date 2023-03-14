"""
This module contains functions for scraping recipes from web links and saving
them in a JSON format.

Functions:
- scrape_and_save_recipes: Scrapes recipes from a CSV file containing web links
and saves them as a JSON file.
"""

import csv
import json
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
