[![build_test](https://github.com/avivamunshi/RecipeGenerator/actions/workflows/build_test.yml/badge.svg)](https://github.com/avivamunshi/RecipeGenerator/actions/workflows/build_test.yml)

Coverage: https://coveralls.io/github/avivamunshi/RecipeGenerator

## Team Members:
Aviva Munshi<br>
Saumya Nauni<br>
Nizan Howard<br>

## Project Overview:

### Project type:
Tool: Web Application (Streamlit Generate a Recipe)
Demo: https://drive.google.com/drive/folders/1ZlpgV7tc2d-A-urfXKiRuAKE2tt-RXYA?usp=sharing

### Questions of interest:
1. How can the recipe be generated randomly?<br>
2. How do we make sure that only one recipe is the output, with many recipes being possible?<br>
3. What additional filters can we have apart from the recipe ingredients? (Can we add label types or filters?) E.g. - cuisine type, calories limit, time duration

### Input/Output:
Input: List of ingredients<br>
Output: one random recipe produced based on input.

### Goal for the project output:
The goal is to build a Streamlit web application that can generate a single recipe using the ingredients the user provides. The output should be a randomly generated recipe that utilizes only the ingredients listed.

### Data sources:
https://www.epicurious.com/<br>
https://www.bonappetit.com/recipes<br>
https://github.com/hhursev/recipe-scrapers<br>

## How to Run the Code
> Setup.py
Steps to follow to install RecipeGenerator

Run 'pip install git+https://github.com/avivamunshi/RecipeGenerator.git'

The package is installed!
You can open a Python interactive session by running the 'python' command in your terminal to verify that it is installed.
Import your package by running the following command:
> From RecipeGenerator  import recipe

### File Description
The structure of the code for how we upload and have our file system:
#### structure
```
RecipeGenerator/
├── LICENSE
|__ Setup.py
├── doc/
  |- Component Specification.md
  |- Functional Specification.md
  |- Technology Review Presentation.pdf
  |- Recipe Final Presentation.pdf
|__ .github/workflows/
  |_ build_test.yml
|—- environment2.yml
├── README.md
|__ example
   |_ Base_user_input.jpeg
   |_ auto_generate_recipe.jpeg
   |- recipe_generate.jpeg
|── recipe /
    |__code/
        ├── ____init__.py
	|__ recipe-scrapers
        |-— app.py
        └── collect.py
	└── map.py
        |__recipe_json_list.txt
        |__ web_links.csv
     └── tests/
         ├── ____init__.py
	 |__ test_collect.py
         |__ test_map.py
	 |__ web_links.csv
```
###  License
Justification for using the MIT License:

In the case of RecipeGenerator, using the MIT License can be beneficial for several reasons. Firstly, the project aims to address a common problem that many people face: the difficulty of deciding what to cook with the ingredients they have at home. Using the MIT License, you can make the project accessible to a wider audience, encouraging others to contribute and improve the code, ultimately resulting in a better user experience for everyone.

Secondly, the project is designed to be a streamlined web app that generates recipes from a collection of recipes based on the user's input of ingredients. By making the project open source, you can encourage others to build upon the codebase and create new features, which can enhance the app's functionality and attract more users.

In summary, the MIT License can be a good choice for RecipeGenerator as it can promote collaboration, encourage contributions from others, and help grow the user base, ultimately leading to a better experience for all users.

### Core Functionality:

##### collect.py
This module includes a set of functions that search through a URL search page and collects recipe links written into a CSV file.
Function obtain_links
The function collects a set of web links from a website. The function takes url_baselink, a string URL web link, as a parameter. The function returns a set of strings that are URL links.

Function link_store_file
The function writes a set of strings in a CSV file. The function takes a set of strings,set_links, as a parameter. The function returns none and is void since the process is writing a file in your file system.

The output of this is written to web_links.csv, which is written to the code folder and is needed for the next component, map.py

##### map.py
This module contains functions for finding recipes based on a list of ingredients.

Firstly, you will notice that the code to generate the file recipe_json_list.txt has been commented out. You need to run this to implement this project, so kindly uncomment it. You only have to run it once and obtain the text file. After this, you can comment on it again and run the rest of the code. We've commented on it to save time, as we're reading the data directly from the relative path in the text file.

Function find_recipe
This function finds a recipe that includes all the specified ingredients.
Args: ingredients (str): A comma-separated string of ingredients.
Refresh (bool, optional): Whether to randomly shuffle the recipe list—defaults to False.
Returns:
Dictionary or None: A dictionary representing the matching recipe or None if no recipe was found.

Further, the try-except block raises:
FileNotFoundError: If the recipe data file cannot be found.
JSON.JSONDecodeError: If the recipe data file cannot be decoded.

The output dictionary is the input for the streamlit app, app.py

##### app.py
app.py
This is our streamlit app, and you need to run the command "streamlit run streamlit.py" in your command prompt to execute it.
Note - you'll need streamlit installed in your file system for this!


