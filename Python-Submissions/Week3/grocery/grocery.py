list_items = {}
while True:
    try:
        item = input()
    except EOFError:
        break
    item = item.upper().strip()
    if item in list_items:
        list_items[item] += 1
    else:
        list_items[item] = 1
for keys in sorted(list_items):
    print(list_items[keys] , keys)

