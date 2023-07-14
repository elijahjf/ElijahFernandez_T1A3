import json
import pyfiglet
from rich.console import Console

console = Console()

def main():
    try:
        # Initialize recipe list
        recipe_list = []
        with open("recipes.json", "r") as infile:
            recipe_list = json.load(infile)
    except FileNotFoundError:
        print("The 'recipes.json' file is not found...")
        print("Creating a new recipe book...")
        recipe_list = []

    selection = 0
    while selection != 4:
        # title = pyfiglet.figlet_format("\n🥢CULINARY CONSOLE🥢\n", font= "slant")
        # print(title)
        console.print("\n🥢CULINARY CONSOLE🥢\n", style="bold green")
        print("Enter a number to navigate the menu...\n")
        print("1. Add recipe")
        print("2. Search recipe")
        print("3. Display recipes")
        print("4. Exit\n")
        selection = int(input())

        if selection == 1:
            def add_recipe():
                console.print("Adding a recipe...", style="blue")
                name_recipe = input("Enter the name of the recipe: ")
                name_author = input("Enter the author of the recipe: ")
                name_cuisine = input("Enter the cuisine of the recipe: ")
                # name_prep_time = input("Enter the prep time of the recipe in minutes: ")
                # name_prep_time = name_prep_time + " mins"
                # name_cook_time = input("Enter the cook time of the recipe in minutes: ")
                name_total_time = input("Enter the total time of the recipe in minutes: ")
                name_servings = input("Enter the servings of the recipe: ")

                # Multi-line input for ingredients
                print("Enter the ingredients of the recipe (type 'end' on a new line to finish):")
                name_ingredients = []
                line = input()
                while line.lower() != "end":
                    name_ingredients.append(line)
                    # list comprehension
                    name_ingredients = [i.lower() for i in name_ingredients]
                    line = input()

                # Multi-line input for method
                print("Enter the method of the recipe (type 'end' on a new line to finish):")
                name_method = []
                line = input()
                while line.lower() != "end":
                    name_method.append(line)
                    # list comprehension
                    name_method = [i.lower() for i in name_method]
                    line = input()

                recipe_list.append([
                    name_recipe.lower(), 
                    name_author.lower(), 
                    name_cuisine.lower(), 
                    name_total_time.lower(), 
                    name_servings.lower(), 
                    name_ingredients, 
                    name_method
                ])
                # list comprehension
                #recipe_list = [i.lower() for i in recipe_list]
            add_recipe()

        elif selection == 2:
            def search_recipes():
                console.print("Searching for a recipe...", style="blue")
                keyword = input("Search: ")
                for i in recipe_list:
                    if keyword in i or any(keyword in ingredient for ingredient in i[6]):
                        print(i) 
            search_recipes()    
                # keyword = input("Search: ")
                # for i in recipe_list:
                #     if keyword in i or keyword in any(keyword in ingredient for ingredient in i["ingredients"]):
                #         print(i)

                # keyword = input("Search: ")
                # for recipe in recipe_list:
                #     if keyword in recipe["name"] or any(keyword in ingredient for ingredient in recipe["ingredients"]):
                #         print(recipe)

                # keyword = input("Search: ")
                # for i in recipe_list:
                #     if keyword in i[0] or i[1] or i[2] or i[3] or i[4] or i[5] or any(keyword in ingredient for ingredient in i[6]):
                #         print(i)

        elif selection == 3:
            def display_all_recipes():
                console.print("Displaying full recipes...", style="blue")
                for i in range(len(recipe_list)):
                    print(recipe_list[i])
            display_all_recipes()

        else:
            def exit():
                console.print("Exiting App...\n", style="red")
            exit()

    bye = pyfiglet.figlet_format("Goodbye!", font= "slant")
    print(bye)

    # Saving to JSON file
    with open("recipes.json", "w") as outfile:
        json.dump(recipe_list, outfile)
    
# if the name of the file = to the main func then go ahead and execute main func
if __name__ == "__main__":
    main()

# add amounts (1cup of flour) that can be changed if you change servings