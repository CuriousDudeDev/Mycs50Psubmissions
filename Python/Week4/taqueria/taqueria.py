menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
final_menu = {}
for key , value in menu.items():
    final_menu[key.lower()] = value
total = 0
while True:
    try:
        item = input('Item: ')
        item = item.lower()
    except EOFError:
        break
    try:
        total += final_menu[item]

    except KeyError:
        pass
    else:
        print(f"Total: ${total}")

