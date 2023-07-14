# Help Documentation
## Steps to install:
1. download zip file from: https://github.com/elijahjf/elijahfernandez_T1A3
2. unzip
3. in terminal navigate to "elijahfernandez_T1A3\src"
4. enter "ls -a" into the terminal to show all files including hidden ones in the src folder
5. run the file script.sh
6. if you're having a permissions error, type in "chmod -x script.sh"
7. do the same to run tests

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
![trello_overview](/trello_terminal_t1a3.png)
![trello_packages](/trello_packages.png)
![trello_readme](/trello_readme.png)