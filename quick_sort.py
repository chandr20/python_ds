from random import randint
unsorted_list =  [1,2,3,4,5,6,7,100,99,88,77,56,42,12]

print(unsorted_list)
def quick_sort(a):
    if len(a) <=1:
        return a

    pivot = a[0]
    smaller = []
    equal = []
    larger = []
    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quick_sort(smaller)+equal+quick_sort(larger)


print(quick_sort(unsorted_list))


