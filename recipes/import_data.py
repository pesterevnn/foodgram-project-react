import json
from .models import Ingredient


if __name__ == '__main__':

    with open('data_for_load/ingredients.json') as json_data:
        data = json.load(json_data,)

    for item in data:
        title = item['title'].replace('"', '`')
        new_ingredient = Ingredient(title=title, dimension=item['dimension'])
        new_ingredient.save()
