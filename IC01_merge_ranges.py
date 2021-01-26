def merge_ranges(items):
    items = sorted(items)
    inventory = []
    while items:
        if not inventory:
            inventory.append(items.pop(0))
        next = items.pop(0)
        if inventory[-1][0] < next[0] and inventory[-1][1] > next[1]:
            continue
        elif inventory[-1][1] >= next[0]:
            new = (inventory.pop()[0], next[1])
            inventory.append(new)
        else:
            inventory.append(next)
    return inventory

        

print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))