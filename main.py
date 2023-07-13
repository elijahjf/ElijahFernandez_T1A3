import json

def main():
    

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
            name_total_time = input("Enter the total time of the recipe in minutes: ")
            name_servings = input("Enter the servings of the recipe: ")

            # Multi-line input for ingredients
            print("Enter the ingredients of the recipe (type 'end' on a new line to finish):")
            name_ingredients = []
            line = input()
            while line != "end":
                name_ingredients.append(line)
                line = input()

            # Multi-line input for method
            print("Enter the method of the recipe (type 'end' on a new line to finish):")
            name_method = []
            line = input()
            while line != "end":
                name_method.append(line)
                line = input()

            recipe_list.append([name_recipe, name_author, name_cuisine, name_total_time, name_servings, name_ingredients, name_method])
        elif selection == 2:
            print("Searching for a recipe...")
            keyword = input("Search: ")
            for i in recipe_list:
                if keyword in i or any(keyword in ingredient for ingredient in i[6]):
                    print(i)

        elif selection == 3:
            print("Displaying full recipes...")
            for i in range(len(recipe_list)):
                print(recipe_list[i])
        else:
            print("Exiting App...")
    print("\nGoodbye!") 
    
# if the name of the file = to the main func then go ahead and execute main func
if __name__ == "__main__":
    main()

# add amounts (1cup of flour) that can be changed if you change servings
