list_items = {}
while True:
    item = input()
    item.upper().strip()
    if list_items[item]:
        list_items[item] += 1
    else:
        