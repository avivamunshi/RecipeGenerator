# Functional Specification

## Background

The problem that this Streamlit web application aims to address is the challenge of meal planning and recipe selection when using a limited set of ingredients. Many people need help finding new and exciting ways to use the ingredients they have on hand and may become bored with their usual repertoire of recipes.

The solution offered by this application is to generate a single recipe that utilizes only the ingredients provided by the user while possibly offering additional filters to customize the recipe to the user's preferences. By randomly generating a recipe based on the input ingredients and other user choices, the application can provide a fun and surprising way to discover new recipes and break out of cooking ruts. Additionally, the option to filter recipes that fit their specific dietary needs and time constraints does meal planning and cooking more efficient and enjoyable.

Overall, this application aims to offer a simple, user-friendly solution to the challenge of meal planning and recipe selection while providing a fun and engaging way to discover new recipes and experiment with different cuisines and ingredients.

## User Profile

The target users of this Streamlit web application are individuals who want to cook at home and are looking for a recipe with the ingredients they currently have at home without having to buy them. They may also have specific dietary needs or preferences that they want to consider when selecting recipes.

In terms of their computing knowledge, users of this application are expected to have basic computer skills, such as browsing the web and using web-based applications. They should also be comfortable using a simple user interface to input their ingredients and other preferences. The application is designed to be user-friendly and accessible to a broad range of users with varying levels of computing expertise. It provides a simple and intuitive interface that guides users through the recipe generation process and offers helpful tips and suggestions.

## Data Sources

1. [Recipe Ingredients Dataset](https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset?select=test.json): This dataset contains an extensive collection of recipes along with their ingredients and nutritional information. The dataset is typically structured as a CSV file or a relational database with tables for recipes and ingredients, which can be queried using Python.

2. [Recipe Box](https://eightportions.com/datasets/Recipes/#fn:1): Recipe Box is a web-based platform that offers a collection of user-generated recipes. The platform allows users to search for and save recipes and provides features such as meal planning and grocery list creation. The data is structured as a web-based application and can be accessed using an API.

3. [Yum.Computer](https://yum.computer/Recipes): Yum.computer is a website that offers a collection of recipes, user ratings, and reviews. The data is structured as a web-based application and can be accessed using web scraping techniques.

4. [Epicurious](https://www.epicurious.com/): Epicurious is a website that offers an extensive collection of recipes, along with user ratings and reviews. The data is structured as a web-based application and can be accessed using web scraping techniques.

5. [Food.com](https://www.food.com/): Food.com is a website that offers a collection of recipes, along with user ratings and reviews. The data is structured as a web-based application and can be accessed using web scraping techniques.

6. [All Recipes](https://www.allrecipes.com/): Allrecipes.com is a website that offers an extensive collection of recipes, along with user ratings and reviews. The data is structured as a web-based application and can be accessed using web scraping techniques.

7. [Bon Appétit](https://www.bonappetit.com/recipes): Bon Appétit is a website that offers a collection of recipes, along with user ratings and reviews. The data is structured as a web-based application and can be accessed using web scraping techniques.

8. [Food Network](https://www.foodnetwork.com/recipes/): Food Network is a website that offers a collection of recipes, along with user ratings and reviews. The data is structured as a web-based application and can be accessed using web scraping techniques.

9. [Taste of Home](https://www.tasteofhome.com/recipes/): Taste of Home is a website that offers a collection of recipes, along with user ratings and reviews. The data is structured as a web-based application and can be accessed using web scraping techniques.

## Use Cases

### 1. Generating a Recipe for a Specific amount of ingredients

>**Explicit Use Case #1:**
>
>Objective: The user receives a recipe that includes the ingredients they provide upon input
>
>1. The generator prompts the user to type in the ingredients they have
>
>2. User types into the generator their input ingredients
>
>3. The generator checks that the input ingredients are valid for human consumption
>
>If the input ingredients are valid:
>
>>Generator displays a recipe from the internet that includes the ingredients listed
>
>If the input ingredients are not valid:
>>Generator displays an error message and reports that it could not find a recipe for the listed ingredients

>**Implicit Use Case #1:**
>
>1. The user navigates to the web application, types in the ingredients they have and clicks the “Find Recipe” button.
>
>2. The generator receives the input from the user, searches the internet for a recipe that has all the ingredients mentioned and returns that recipe to the user.
>
>3. The recipe consists of instructions on how to make the dish using the ingredients provided by the user
>
>4. The user then uses the instructions mentioned in the recipe and prepares the dish

### 2. Generating a Recipe for a Dietary Requirement

>**Explicit Use Case #2:**
>
>Objective: The user receives a recipe that matches their specific dietary requirement.
>
>1. The user navigates to the web application and selects the "Generate Recipe" option.
>
>2. The application prompts users to select their dietary requirements (e.g., vegetarian, vegan, gluten-free).
>
>3. The user selects their dietary requirement.
>
>4. The application prompts the user to enter the ingredients they have on >hand and the desired meal time.
>
>5. The user enters the ingredients they have and the desired meal time.
>
>6. The application searches for a recipe that matches the user's dietary requirement, the provided ingredients, and the desired meal time.
>
>7. The application displays the recipe that matches the user's dietary requirement, uses the provided ingredients, and matches the desired meal time.
>
>8. The application displays relevant information such as cooking time, calories and serving size.


>**Implicit Use Case #2:**
>
>1. The user navigates to the web application and selects the "Generate Recipe" option.
>2. The application prompts the user to select their dietary requirement (e.g. vegetarian, vegan, gluten-free).
>3. The user selects their dietary requirement.
>4. The application prompts the user to enter the ingredients they have on hand and the desired meal time.
>5. The user enters the ingredients they have and the desired meal time.
>6. The application searches for a recipe that matches the user's dietary requirement, the provided ingredients, and the desired meal time.
>7. The application displays the recipe that matches the user's dietary requirement, uses the provided ingredients, and matches the desired meal time.
>8. The user reviews the recipe and relevant information such as cooking time, calories and serving size.

