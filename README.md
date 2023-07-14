# [vimeo](https://vimeo.com/user197620247)
# [github](https://github.com/elijahjf/elijahfernandez_T1A3)

# Coding Conventions
Pep8

# Help Documentation
## Steps to install:
1. download zip file from: https://github.com/elijahjf/elijahfernandez_T1A3
2. unzip
3. in terminal navigate to "elijahfernandez_T1A3\src"
4. enter "ls -a" into the terminal to show all files including hidden ones in the src folder
5. run the file setup.sh
6. run the file run.sh
7. if you're having a permissions error, type in "chmod -x script.sh"
8. do the same to run tests

## Dependencies required by the application to operate
## System/hardware requirements
- Ensure you have Python 3 and pip3 installed on your computer.
- Using a UNIX supporting terminal
- computer's administor permissions
## How to use any command line arguments made for the application

# Features

## A Recipe Book

### Menu with options to:
```
Add a new recipe: adding a recipe involves inputting the following details into a list:

- recipe name
- author name
- type of cuisine
- total time the recipe takes
- number of servings
- ingredients (this is a nested list)
- method (this is a nested list)


Search recipe database:

using search terms input such as recipe name, author, cuisine, total time, servings, and     ingredients. (this searches the recipe list and the ingredients list, and not the method list)
output matched terms and all the details associated.
for example:

Search Term Input: Eggs

Output:
[["cookies", "mum", "dessert", "120", "4", ["butter", "milk", "sugar", "flour", "eggs"], ["mix dry", "mix wet", "make balls", "put in oven for 20"]], ["scrambled eggs", "mum", "breakfast", "10", "1", ["eggs", "seasoning", "oil"], ["break eggs in oiled pan", "scramble", "season"]]]


Display all recipes

Output: displays all recipes


Exit
```
Recipe data is store in a JSON file. This will be read by the application on start

## Planning
I utilised trello boards to manage my projects lifecycle and iteration. I made nested checklists, updated with comments, and left links and descriptions.
![trello_overview](/docs/trello_terminal_t1a3.png)
![trello_packages](/docs/trello_packages.png)
![trello_readme](/docs/trello_readme.png)

## Testing
![pytest_pass](/docs/pytest_pass.png)
### Test 1: test_file_creation:
- Ensure that a file is created when the create_recipe_file function is called.
- The test checks if the file doesn't exist before calling the function, and then verifies that the file exists after the function is executed.

#### Feature Covered
The first test verifies the file creation functionality of the application.

#### What is Being Tested
This test checks whether the create_recipe_file function successfully creates a file when called.

#### Test Cases and Expected Results
##### Test Case: File doesn't exist before the function call
Expected Result: The file should be created after calling the create_recipe_file function.
##### Test Case: File already exists before the function call
Expected Result: The file should still be created and overwritten with an empty file.

### Test 2: test_add_recipe:
- Test the process of adding a recipe to the recipe list and saving it to a file.
- The test creates a file, loads the recipe list from the file, adds a sample recipe to the list, and saves the updated list back to the file.
- It then checks if the added recipe is present in the loaded list by comparing various attributes of the recipe.

#### Feature Covered
The second test validates the process of adding a recipe to the recipe list and saving it to a file.

#### What is Being Tested
This test ensures that the application correctly handles adding a recipe, updating the recipe list, and saving it to a file.

#### Test Cases and Expected Results
##### Test Case: Adding a recipe to an empty list
Expected Result: The recipe should be successfully added to the list, and the updated list should be saved to the file.

##### Test Case: Adding a recipe to a non-empty list
Expected Result: The recipe should be appended to the existing list, and the updated list should be saved to the file.
Including this testing procedure with the source code of the application helps provide a clear understanding of the specific features covered, what is being tested, and the expected results for each test case.
