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
            recipe_list.append([name_recipe, name_author, name_cuisine])
        else:
            print("Exiting App...")
    print("\nGoodbye!") 
    
# if the name of the file = to the main func then go ahead and execute main func
if __name__ == "__main__":
    main()
