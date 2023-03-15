"""Module to test the 'find_recipe' function from the 'final_mapping_code' module."""
import unittest
import sys
import os
from unittest.mock import mock_open, patch
#sys.path.insert(1, f"{os.getcwd()}/Code")

from code.map import find_recipe #pylint: disable=import-error

#from pathlib import Path
os.chdir("../")
sys.path.append(f"{os.getcwd()}/Code/")

class TestFindRecipe(unittest.TestCase):
    """Test class for the find_recipe function"""
    def setUp(self):
        self.ingredients = 'milk, eggs'

    def test_one_shot_1(self):
        """Test that a recipe is returned when ingredients are found in the recipe"""
        with patch('builtins.open', mock_open(read_data='[{"ingredients": ["milk", "eggs"]}]')):
            recipe = find_recipe(self.ingredients)
            self.assertIsNotNone(recipe)

    def test_one_shot_2(self):
        """Test that None is returned when no recipe is found"""
        with patch('builtins.open', mock_open(read_data='[{"ingredients": ["flour", "sugar"]}]')):
            recipe = find_recipe(self.ingredients)
            self.assertIsNone(recipe)

    def test_smoke_1(self):
        """Test that recipe data file is found"""
        with patch('builtins.open', mock_open(read_data='[{"ingredients": ["milk", "eggs"]}]')):
            recipe = find_recipe(self.ingredients)
            self.assertIsNotNone(recipe)

    def test_smoke_2(self):
        """Test that the find_recipe function returns the expected output"""
        with patch('builtins.open', mock_open(
        read_data='[{"name": "French Toast", "ingredients": ["milk", "eggs", "bread"]}]'
    )):
            expected_output = {"name": "French Toast", "ingredients": ["milk", "eggs", "bread"]}
            recipe = find_recipe(self.ingredients)
            self.assertEqual(recipe, expected_output)


    def test_edge_1(self):
        """Test that recipe is returned when ingredients are substrings of recipe ingredients"""
        with patch('builtins.open', mock_open(
            read_data='[{"ingredients": ["whole-milk", "large eggs"]}]'
    )):
            recipe = find_recipe(self.ingredients)
            self.assertIsNotNone(recipe)

    def test_edge_2(self):
        """Test that recipe is returned when ingredients are uppercase"""
        with patch('builtins.open', mock_open(read_data='[{"ingredients": ["MILK", "EGGS"]}]')):
            recipe = find_recipe(self.ingredients)
            self.assertIsNotNone(recipe)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            find_recipe("non_existent_file.txt")


if __name__ == '__main__':
    unittest.main()
