from main import *
import os
import json

def create_recipe_file(file_path):
    # create empty file
    with open(file_path, "w") as outfile:
        json.dump([], outfile)

def load_recipe_list(file_path):
    # load list from file
    with open(file_path, "r") as infile:
        recipe_list = json.load(infile)

    return recipe_list

def test_file_creation(tmp_path):
    json_file_path = os.path.join(tmp_path, "recipes.json")
    assert not os.path.exists(json_file_path)  # ensure file doesn't exist

    # call function to create file
    create_recipe_file(json_file_path)

    assert os.path.exists(json_file_path)  # ensure file is created

def test_add_recipe(tmp_path):
    json_file_path = os.path.join(tmp_path, "recipes.json")
    assert not os.path.exists(json_file_path)  # ensure file doesn't exist

    # create file and load list
    create_recipe_file(json_file_path)
    recipe_list = load_recipe_list(json_file_path)

    # add sample recipe to list
    recipe_list.append([
        "Recipe Name",
        "Author Name",
        "Cuisine Type",
        "60",
        "4",
        ["Ingredient 1", "Ingredient 2"],
        ["Step 1", "Step 2"]
    ])

    # save updated list to file
    with open(json_file_path, "w") as outfile:
        json.dump(recipe_list, outfile)

    # check if added recipe is present in list
    updated_recipe_list = load_recipe_list(json_file_path)

    assert len(updated_recipe_list) == 1
    assert updated_recipe_list[0][0] == "Recipe Name"
    assert updated_recipe_list[0][1] == "Author Name"
    assert updated_recipe_list[0][2] == "Cuisine Type"
    assert updated_recipe_list[0][3] == "60"
    assert updated_recipe_list[0][4] == "4"
    assert updated_recipe_list[0][5] == ["Ingredient 1", "Ingredient 2"]
    assert updated_recipe_list[0][6] == ["Step 1", "Step 2"]
