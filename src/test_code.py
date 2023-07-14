import json
from main import *

def test_create_json(tmp_path):
    # # make sure json doesn't exist before testing
    # assert not (tmp_path / "recipes.json").exists()

    # main()

    # # make sure json is created after testing
    # assert (tmp_path / "recipes.json").exists()

    recipes_file_path = tmp_path / "recipes.json"
    assert not recipes_file_path.exists()

    main()

    assert recipes_file_path.exists()