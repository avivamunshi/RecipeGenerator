# Component Specification

## Component 1: Database of Recipes

**Name:** Recipe Database

**What it does:** Collects recipes from webpages and stores them in a dictionary.

**Inputs:** A subset of web pages that have recipes ( web recipe links )

**Preliminary Output:** List of dictionaries that includes recipes and links to the original web page. Each dictionary has a key ( the web link)
***Curren Output**
Saves a set of url web links into a csv bypassing the
time request constraints and proxy all
Webl_links.csv is wriiten the directry of the code.
## Component 2: Webpage to collect user input

**Name:** Web App

**What it does:** Provides an interface to collect the inputs from the user

**Inputs:**
 Dietary Requirements (a string in the form of options)
Ingredients (a string) user case

**Outputs:** A recipe that uses the ingredients mentioned that is called from running an import from the map.py fille

**Assumptions:**
The ingredients should be food items with the assumption that the basic condiments are a staple in everyone’s pantry
There should be at least 3-4 ingredients listed to get an appropriate recipe

## Component 3: Mapping User input to Database to webpage output

**Name:** Input-Output Mapper

**What it does:** Maps user inputs from the Web App to the corresponding database entries and retrieves the corresponding webpage output.

**Inputs:**
User input from the Web App (e.g. ingredients, image, url, instructions, title)
Csv file of the collected url web links of 300 to 400 recipe links.

**Outputs:**
Webpage output containing the recipe that meets the user's input criteria (e.g. recipe name, ingredients, preparation instructions) Returning a json file of a dictonary. to be use in the streamlit

**Assumptions:**

The database contains all necessary recipe information to satisfy user input criteria.
The database can handle multiple user requests simultaneously.
User input is sanitized and validated to prevent SQL injection and other security risks.
The Github recipe_scrapers package takes the
an individual url web link and extracts the information correctly

# Specification for each component

## Component 1: Database of Recipies

1. Packages: Beautiful Soup
2. Modules: importing urlib, python request
3. Resources: recipe box is an open source that explains a similar step process
4. Data: Web links of recipe websites

**Functions:** two sub-functions, one to collect from a web link  and the other to store recipe text

**Pre_Components:**
There are no already made components except having recipe web links preplanned already, and the only sub-component is splitting the task into two sub-functions.

## Component 2: Webpage to collect user input

1. Packages: Streamlit
2. Resources: Streamlit Documentation
3. Functions:
    - Def_app: the basic structure of the web app
    - Def_style: to define the style of images, links, etc

## Component 3: Mapping User input to Database to webpage output

1. Packages: recipe_scrapers scrape me, Streamlit,
2. Modules: importing os csv json random
and attachement of the Github package repository.
3. Resources: Recipe Scrapers  is an open source github package that extracts the indivual tags of components of url web site   Streamlit Documentation
4. Data: Web links of recipe websites
5. Functions:
    - Reads in a web links csv file
    that is the collection of recipes from
    bonappetit and epicurious.
    - find_recipe(ingredients, refresh=False):
    Find a recipe that includes all the specified ingredients.
    - Args:
        ingredients (str): A comma-separated string of ingredients.
        refresh (bool, optional): Whether to randomly shuffle the recipe list. Defaults to False.
    Further the try-except block raises:
    FileNotFoundError: If the recipe data file cannot be found. json.JSONDecodeError: If the recipe data file cannot be decoded.

6. Pre_Components:
    - A database of recipes (created in Component 1) with web links and associated ingredients
    - A web page to collect user input (created in Component 2)
    - Git Hub package recipe_scrapers import scrape_me
    that looks into the recipes and collects the tag
    of each component encoded in the html proccess

#  Pre_Pseudocode

```
Functions:
old Process
  get_recipe_from_link(link):
      # Given a recipe link, this function extracts relevant data and returns a dictionary with the recipe information
      recipe = {}
      # Use requests and Beautiful Soup to fetch and parse the HTML content of the recipe link
      html_content = requests.get(link).content
      soup = BeautifulSoup(html_content, 'html.parser')

      # Extract relevant information from the HTML using Beautiful Soup selectors
      recipe['title'] = soup.select('h1')[0].text
      recipe['image'] = soup.select('img')[0]['src']
      recipe['ingredients'] = [li.text for li in soup.select('ul.ingredient-list li')]
      recipe['instructions'] = [li.text for li in soup.select('ol.instruction-list li')]

      return recipe

  store_recipe(recipe):
      # Given a dictionary of recipe information, this function stores it in the database
      # Here, we'll just print the recipe information to simulate storing it
      print(f"Storing recipe:\n{recipe}\n")

Current Process:
recipe_json_list = []

# get the absolute path of the directory containing this script
function_dir = os.path.dirname(os.path.abspath(__file__))

# construct the path to the CSV file using the script directory as the base path
csv_path = os.path.join(function_dir, '../Code/web_links.csv')

# check if the CSV file exists before proceeding
if os.path.exists(csv_path):
    with open(csv_path, encoding='utf-8') as file:
        reader = csv.reader(file)
        recipe_json_list = []
        for row in reader:
            url = row[0]
            scraper = scrape_me(url, wild_mode=True)
            recipe_json_list.append(scraper.to_json())
```

# Interaction Diagram

![Figure](/images/Interactive.jpeg)

# Milestone (Preliminary Plan):

1. Build a database of recipes.
    - Success: a database of recipes can be accessed by a function a call returning a list of dictionaries.
2. Build a user interface web application via Streamlit
	- Success: a web page that can take user input and return a list of strings on the backend
3. Display a webpage output of a picture and recipe instructions
    - Success: maps ingredients from the user to a recipe from the database and outputs the recipe picture, instructions, and original weblink.

## Task Order
Tasks one and two can be implemented without a required order; however, task three needs tasks one and two to be completed to run a display.
Therefore the task is split into three categories:

### **First Week**

**Build a database of recipes.**

The first task as a team is to build the database. We need beautiful soup, Urlib request package, and test validations of prox sever access denial, error, or time requests for web links.

### **Second week**

**Build a user interface web application via Streamlit**

The second task as a team is to build the web application; we need the Streamlit web application and add user interface tabulation such as type and input from the user. In test cases on display online, the correct output type returns a list of strings and a fixed amount of input required e,g (3-4 ingredients).

### **Third Week**

**Display a webpage output of a picture and recipe instructions.**

The third task will also be tackled as a team, and first needs the assigned task in weeks one and two to be completed. The packages necessary are beautiful soup and Streamlit.  Test validations will include an assert for an output display, a string of recipe instructions, and a test for display order and heading.