def merge_lists(l1, l2, sorted_list=[]):
    if not l1:
        sorted_list = sorted_list + l2
        l2 = False
    if not l2:
        sorted_list = sorted_list + l1
        l1 = False
    if not l1 and not l2:
        return sorted_list
    else:
        if l1[0] < l2[0]:
            sorted_list.append(l1.pop(0))
        elif l2[0] < l1[0]:
            sorted_list.append(l2.pop(0))
        return merge_lists(l1, l2, sorted_list)


list1 = [3,4,6,10,11,15]
list2 = [1,5,8,12,14,19]

print(merge_lists(list1, list2))


# COMMENTS GLOW

"""

these comments are great too
"""