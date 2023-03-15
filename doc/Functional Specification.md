## Functional Specification

### Background

This Streamlit web application aims to address the challenge of meal planning and recipe selection when using a limited set of ingredients. Many people need help finding new and exciting ways to use the ingredients they have on hand and may become bored with their usual repertoire of recipes.

The solution offered by this application is to generate a single recipe that utilizes only the ingredients provided by the user while possibly offering additional filters to customize the recipe to the user's preferences. By randomly generating a recipe based on the input ingredients and other user choices, the application can provide a fun and surprising way to discover new recipes and break out of cooking ruts. Additionally, the option to filter recipes that fit their specific dietary needs and time constraints does meal planning and cooking more efficient and enjoyable.

Overall, this application aims to offer a simple, user-friendly solution to the challenge of meal planning and recipe selection while providing a fun and engaging way to discover new recipes and experiment with different cuisines and ingredients.

### User Profile

The target users of this Streamlit web application are individuals who want to cook at home and are looking for a recipe with the ingredients they currently have at home without having to buy them. They may also have specific dietary needs or preferences that they want to consider when selecting recipes.

In terms of their computing knowledge, users of this application are expected to have basic computer skills, such as browsing the web and using web-based applications. They should also be comfortable using a simple user interface to input their ingredients and other preferences. The application is designed to be user-friendly and accessible to a broad range of users with varying levels of computing expertise. It provides a simple and intuitive interface that guides users through the recipe generation process and offers helpful tips and suggestions.

### Data Sources

1. [Recipe Ingredients Dataset](https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset?select=test.json): This dataset contains an extensive collection of recipes along with their ingredients and nutritional information. The dataset is typically structured as a CSV file or a relational database with tables for recipes and ingredients, which can be queried using Python.

2. [Recipe Box](https://eightportions.com/datasets/Recipes/#fn:1): Recipe Box is a web-based platform that offers a collection of user-generated recipes. The platform allows users to search for and save recipes and provides meal planning and grocery list creation features. The data is structured as a web-based application and can be accessed using an API. However, this is  no longer used due to an issue of depreciation in new website URL collections.

3. [Epicurious](https://www.epicurious.com/): Epicurious is a website that offers an extensive collection of recipes, along with user ratings and reviews. The data is structured as a web-based application and can be accessed using web scraping techniques.

4. [Bon Appétit](https://www.bonappetit.com/recipes): Bon Appétit is a website that offers a collection of recipes, along with user ratings and reviews. The data is structured as a web-based application and can be accessed using web scraping techniques.

5. [Recipe Scrape](https://github.com/hhursev/recipe-scrapers): Git hub package
that takes a web link URL and extracts the tag contents from one particular page. Following
from recipe_scrapers import scrape_me

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
>1. The user navigates to the web application, types in their ingredients, and clicks the "Find Recipe" button.
>
>2. The generator receives the input from the user, searches the internet for a recipe with all the ingredients mentioned, and returns that recipe to the user.
>
>3. The recipe consists of instructions on how to make the dish using the ingredients provided by the user
>
>4. The user then uses the instructions mentioned in the recipe and prepares the dish

### 2. Generating a Recipe for a Dietary Requirement

>**Explicit Use Case #2:**
>
>Objective: The user receives a recipe matching their dietary requirement.
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
>8. The application displays relevant information such as cooking time, calories, and serving size.


>**Implicit Use Case #2:**
>
>1. The user navigates to the web application and selects the "Generate Recipe" option.
>
>2. The application prompts the user to select their dietary requirement (e.g., vegetarian, vegan, gluten-free).
>
>3. The user selects their dietary requirement.
>
>4. The application prompts the user to enter the ingredients they have on hand and the desired meal time.
>
>5. The user enters the ingredients they have and the desired meal time.
>
>6. The application searches for a recipe that matches the user's dietary requirement, the provided ingredients, and the desired meal time.
>
>7. The application displays the recipe that matches the user's dietary requirement, uses the provided ingredients, and matches the desired meal time.
>
>8. The user reviews the recipe and relevant information such as cooking time, calories, and serving size.

## Updates to Application Functional Specification

#### Limitations:  Overall Objective vs. Current Application:
#### Use Case 1 Current

 Our overall user Objective: The user receives a recipe that includes the ingredients they provide upon input.
Currently, the recipe generator application meets the use case and can return the recipe with only the listed ingredients. Even super exceeding this specification to auto-generate a new recipe if the desired recipe generator is not in the user's presence.

#### Use Case 2 Current

Our overall Objective: The user receives a recipe that matches their specific dietary requirement. We still need to meet this user case test in distinguishing between the dietary requirement to meet the user needs vegan versus vegetarian requirements. An attempt was made through auto-complete in the streamlit web app for the user in its search engine. However, we cannot conclude that aspect works all the time due to time constraints and web app complexity; further research is necessary to complete the second use case implementation.

#### Time Constraints and Difficulty

> Recipe Box: A git hub package to collect a large volume of weblinks, was depreciated; therefore, we had to implement from scratch a way to get a large volume of web links; we had individually find the nested tag and div classes and patterns, request, and proxy wall passage to get URL web links pushing back functionality.

> Team Size: Because we had a lot more backend work generating data from scratch and track patterns from multiple websites, testing whether the request is a valid URL. It required two people to the backend, allowing the front end to have less help. In that case, much effort in the data engineering component affected the app user center design appearance. However, the code is functional and works; future development would improve the frontend specifications and style. 

> Conda Evn package installment: The recipe scraper git hub package
 had a lot of co-packages and functionality that made the delay in implementing a more straightforward approach for each dependency. Extending conda activates

> Conda Evn package installment: The streamlit web package had a lot of co-packages and functionality that made the delay in implementing a simpler
 the approach of each dependency.


### Justifications



#### Pylint Disablement:

#### When you navigate to RecipeGenerator > recipe > code > map.py pylint disable the import error

>We disabled pylint's import-error check in line 5 because the module 'recipe_scrapers' was not recognized by pylint. This module is a third-party library used for web scraping, which is necessary for the script to work. Therefore, we needed to disable pylint's import-error check to prevent the script from producing an unnecessary warning.

#### Commented-out code for generating recipe_json_list.txt:

>The code for generating the recipe_json_list.txt file has been commented out because it takes approximately 21 minutes to run due to the need to iterate through 400 links. We ran the code once to generate the file, and after that, we just opened the file in the find_recipe function whenever it was needed. By doing this, we saved time by not having to regenerate the file every time the script was run.

#### When you navigate to RecipeGenerator > recipe > code > app.pypylint disable import-error:

>We included this statement because pylint was flagging an error when importing the find_recipe function from the map module. However, we know this function exists and is accessible in our current environment, so we wanted to suppress this error to avoid confusion and allow our code to run without issue.

#### pylint disable inconsistent-return-statements:

>We included this statement because pylint was flagging an error related to the fact that our generating function does not always return a value. However, in our case, it is intentional that the function only returns a value under certain conditions (i.e., when the "Regenerate Recipe" button is clicked). Therefore, we wanted to suppress this error to ensure that pylint does not raise unnecessary warnings for our code.

#### When you navigate to RecipeGenerator > recipe > tests > test_collect.py pylint: disable=redundant-unit test-assert

>We included the pylint: disable=redundant-unit test-assert in the smoke test because the smoke test is designed to assert that the function under the test is executing without any exceptions or errors. This is typically used to quickly check that the application is in a reasonable state and functioning correctly. In this case, the smoke test is intended to verify that the obtain_links function can execute without any issues, so the assertion statement is intentionally redundant. By including the pylint disable, we ensure that the code passes static analysis checks without flagging this redundant assertion as an issue while keeping the assertion in place as a reminder of the smoke test's purpose.

##### When you navigate to RecipeGenerator > recipe > tests > test_map.py pylint: disable=import-error

>We included the pylint: disable=import-error next to the import statement for the 'find_recipe' function in the 'final_mapping_code' module in our test script because we were getting a warning for 'map' and other related variables. This warning occurred because the test script is running inside the 'Test' folder, but on the backend, we've changed the system path to the 'Code' folder. Therefore, while running, the script looked for the 'map' file inside the 'Test' folder instead of the 'Code' folder. To prevent this warning from interfering with our test results, we disabled the import error for the 'find_recipe' function.

#### Code Refinement:

#### When you navigate to RecipeGenerator > recipe > code > collect.py Commented-out code for generating web_links.csv:

>The code for generating the web_links.csv file has been commented out because it takes a long time to run due to the large volume of data of web scrapping a request. We ran the code once to generate the file, and after that, we just opened the file in the find_recipe function whenever it was needed. By doing this, we saved time by not having to regenerate the file every time the script was run to collect. However, a developer may want twice the amount of data
and since the code will update on every run, we commented this functionality out and let the developers choose to keep it.

#### Unit Testing:

#### Unit testing performed for app.py was deemed unnecessary

>We did not perform unit testing for app.py as it is part of the front end. Unit testing aims to test the functionality of individual modules and functions in isolation from the rest of the application. However, the app.py file is responsible for the application's overall behavior and user interface, making it difficult to test individual components in isolation. Instead, we relied on manual testing and user feedback to ensure that the application was functioning as intended.

#### Continous Integration Resultant coverage justification

>Resultant coverage justification. We ultimately achieved coverage of 89%. It would have crossed 90%, but our coverage was low because we did not unit test our main functions - something that is not required.