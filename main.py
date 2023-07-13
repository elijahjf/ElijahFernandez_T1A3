import json

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
        print("\n🥢CULINARY CONSOLE🥢\n")

        print("Enter a number to navigate the menu...\n")
        print("1. Add recipe")
        print("2. Search recipe")
        print("3. Display recipes")
        print("4. Exit\n")
        selection = int(input())
        
        if selection == 1:
            print("Adding a recipe...")
            name_recipe = input("Enter the name of the recipe: ")
            name_author = input("Enter the author of the recipe: ")
            name_cuisine = input("Enter the cuisine of the recipe: ")
            recipe_list.append([name_recipe, name_author, name_cuisine])
        elif selection == 2:
            print("Searching for a recipe...")
            keyword = input("Search: ")
            for i in recipe_list:
                if keyword in i:
                    print(i)
        elif selection == 3:
            print("Displaying full recipes...")
            for i in range(len(recipe_list)):
                print(recipe_list[i])
        else:         
            print("Exiting App...")
    print("\nGoodbye!") 
    
    # Saving to JSON file
    with open("recipes.json", "w") as outfile:
        json.dump(recipe_list, outfile)

# if the name of the file = to the main func then go ahead and execute main func
if __name__ == "__main__":
    main()
