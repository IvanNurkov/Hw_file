from pprint import pprint

with open("task1\\text.txt", encoding="utf-8") as file:
    cook_book = {}


    for line in file:
        dish = line.strip()
        quantity = file.readline().strip()
        recipe = []

        for line in range(int(quantity)):
            text = file.readline().split(" | ")
            recipe.append({'ingredient_name': text[0], 'quantity': text[1],
                           'measure': text[2].strip()})
        cook_book[dish] = recipe
        file.readline()

pprint(cook_book)

def get_shop_list_by_dishes(dishes, count_person):
    for dish in dishes:
        if dish in cook_book.keys():
            for dict_cook_book in cook_book[dish]:
                mass = dict_cook_book.get('quantity') * count_person *len(dishes)
                print(f"{dict_cook_book.get('ingredient_name')}: ", {f"{mass} {dict_cook_book.get('measure')}"})
        else: 
            print(f'Такого блюда нет')
    
get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)