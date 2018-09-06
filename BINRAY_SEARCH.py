from random import randint

unsorted_list = [randint(0,2) for _ in range(15)]
print(unsorted_list)

def quick_sort(unsorted_list):

    if len(unsorted_list) <=1:
        return unsorted_list
    pivot = unsorted_list[0]
    smaller = []
    larger = []
    equal = []
    for ele in unsorted_list:


        if ele == pivot:
            equal.append(ele)
        elif ele < pivot:
            smaller.append(ele)
        else:
            larger.append(ele)
    return quick_sort(smaller) + equal + quick_sort(larger)







def Binary_search(newlist,val,searchfirst):
    l = 0
    r = len(newlist)-1
    result = -1

    while l <= r:
        mid = (l+r)//2
        if newlist[mid] == val:
            result = mid
            if searchfirst:
                r = mid-1
            else:
                l = mid+1


        elif newlist[mid] < val:
            l = mid+1
        else:
            r = mid-1
    return result


sorted_list = quick_sort(unsorted_list)
print(sorted_list)

first =  Binary_search(sorted_list,2,True)
last =  Binary_search(sorted_list,2,False)
print("Element in found in posistion {}".format(((last-first)+1)))


