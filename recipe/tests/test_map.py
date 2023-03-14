"""Module to test the 'find_recipe' function from the 'final_mapping_code' module."""
import unittest
import sys
import os
import json
from unittest.mock import mock_open, patch
#sys.path.insert(1, f"{os.getcwd()}/Code")

from code.map import find_recipe #pylint: disable=import-error

#from pathlib import Path
os.chdir("../")
sys.path.append(f"{os.getcwd()}/Code/")

# why we're getting a warning for map and other related variables
# the code is running inside the test folder
# but on the backend we've changed the system path to Code
# so while running its looking for the map file inside the Test folder

class TestFindRecipe(unittest.TestCase):
    """Test class for the find_recipe function"""
    # def setUp(self):
    #     self.ingredients = 'milk, eggs'

    # def test_one_shot_1(self):
    #     """Test that a recipe is returned when ingredients are found in the recipe"""
    #     with patch('builtins.open', mock_open(read_data='[{"ingredients": ["milk", "eggs"]}]')):
    #         recipe = find_recipe(self.ingredients)
    #         self.assertIsNotNone(recipe)

    # def test_one_shot_2(self):
    #     """Test that None is returned when no recipe is found"""
    #     with patch('builtins.open', mock_open(read_data='[{"ingredients": ["flour", "sugar"]}]')):
    #         recipe = find_recipe(self.ingredients)
    #         self.assertIsNone(recipe)

    # def test_smoke_1(self):
    #     """Test that recipe data file is found"""
    #     with patch('builtins.open', mock_open(read_data='[{"ingredients": ["milk", "eggs"]}]')):
    #         recipe = find_recipe(self.ingredients)
    #         self.assertIsNotNone(recipe)

    # def test_smoke_2(self):
    #     """Test that the find_recipe function returns the expected output"""
    #     with patch('builtins.open', mock_open(
    #     read_data='[{"name": "French Toast", "ingredients": ["milk", "eggs", "bread"]}]'
    # )):
    #         expected_output = {"name": "French Toast", "ingredients": ["milk", "eggs", "bread"]}
    #         recipe = find_recipe(self.ingredients)
    #         self.assertEqual(recipe, expected_output)


    # def test_edge_1(self):
    #     """Test that recipe is returned when ingredients are substrings of recipe ingredients"""
    #     with patch('builtins.open', mock_open(
    #         read_data='[{"ingredients": ["whole-milk", "large eggs"]}]'
    # )):
    #         recipe = find_recipe(self.ingredients)
    #         self.assertIsNotNone(recipe)

    # def test_edge_2(self):
    #     """Test that recipe is returned when ingredients are uppercase"""
    #     with patch('builtins.open', mock_open(read_data='[{"ingredients": ["MILK", "EGGS"]}]')):
    #         recipe = find_recipe(self.ingredients)
    #         self.assertIsNotNone(recipe)

    def setUp(self):
        """Define a sample recipe data file for testing"""
        self.recipe_data = [
            {
                "name": "Scrambled Eggs",
                "ingredients": ["eggs", "butter", "milk"]
            },
            {
                "name": "Omelette",
                "ingredients": ["eggs", "cheese", "ham"]
            },
            {
                "name": "Pancakes",
                "ingredients": ["flour", "milk", "eggs"]
            }
        ]
        # Save the recipe data as a JSON file for testing
        self.mock_file = json.dumps(self.recipe_data)

    def test_find_recipe_success(self):
        """Test a successful scenario where a matching recipe is found"""
        result = find_recipe('milk, eggs', refresh=False)
        expected = {
            "name": "Scrambled Eggs",
            "ingredients": ["eggs", "butter", "milk"]
        }
        self.assertEqual(result, expected)

    def test_find_recipe_no_match(self):
        """Test a scenario where no matching recipe is found"""
        result = find_recipe('sugar, salt', refresh=False)
        self.assertIsNone(result)

    @patch('builtins.open', new_callable=mock_open, read_data="{}")
    def test_find_recipe_file_not_found(self, mock_file):
        """Test a scenario where the recipe data file is not found"""
        result = find_recipe('eggs, cheese', refresh=False)
        self.assertIsNone(result)
        mock_file.assert_called_once_with('recipe_json_list.txt', 'r', encoding='utf-8')
        self.assertEqual(mock_file().read.call_count, 1)

    @patch('builtins.open', new_callable=mock_open, read_data="invalid json")
    def test_find_recipe_decoding_error(self, mock_file):
        """Test a scenario where the recipe data file cannot be decoded"""
        result = find_recipe('eggs, cheese', refresh=False)
        self.assertIsNone(result)
        mock_file.assert_called_once_with('recipe_json_list.txt', 'r', encoding='utf-8')
        self.assertEqual(mock_file().read.call_count, 1)

    def test_find_recipe_refresh(self):
        """Test a scenario where the recipe list is refreshed"""
        with patch('random.shuffle') as mock_shuffle:
            find_recipe('eggs, cheese', refresh=True)
            mock_shuffle.assert_called_once()

    def test_find_recipe_partial_match(self):
        """Test a scenario where a recipe matches with partial ingredient matches"""
        result = find_recipe('beaten eggs, milk', refresh=False)
        expected = {
            "name": "Scrambled Eggs",
            "ingredients": ["eggs", "butter", "milk"]
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
