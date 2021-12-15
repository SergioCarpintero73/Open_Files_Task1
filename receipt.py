from pprint import pprint


# Задача №1
def cookbook_file(file):
    cook_book = {}
    with open(file) as file:
        for string in file:
            dish = string.strip()
            ingredients = []
            for ingredient in range(int(file.readline())):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredients.append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                )
            cook_book[dish] = ingredients
            file.readline()
    return cook_book


# Задача №2
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    products_list = {}
    for each_ingredients in dishes:
        for product_key in cook_book.get(each_ingredients):
            if product_key.get('ingredient_name') in products_list:
                if products_list[product_key.get('ingredient_name')]['measure'] == product_key.get('measure'):
                    products_list[product_key.get('ingredient_name')]['quantity'] += product_key.get('quantity') * person_count
            else:
                products_list[product_key.get('ingredient_name')] = dict(measure=product_key.get('measure'), quantity=product_key.get('quantity') * person_count)
    return products_list


def main():
    cookbook = cookbook_file('recipes.txt')
    products = get_shop_list_by_dishes(cookbook, ['Запеченный картофель', 'Омлет'], 2)
    pprint(products)


main()