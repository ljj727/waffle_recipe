from waffle_recipe.recipe import Ingredients

def test_ingredients():
    ingredients = Ingredients(repo="/home/ljj/ws/dvc_test")
    ingredients.download()
    ingredients.upload()
    ingredients.info()
    ingredients.waffle_info()
    print(ingredients)
    assert ingredients.repo == "/home/ljj/ws/dvc_test"