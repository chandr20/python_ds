Sample_list = [10,20,40,70,80,90,100,120,170,160]





def binary_search(newlist,val):
    l = 0
    h = len(newlist)-1

    while l <= h:
        mid = (l+(h-1))//2
        if newlist[mid] == val:
            return mid
        elif newlist[mid] < val:
            l = mid+1
        else:
            r = mid-1
    return -1




print(binary_search(Sample_list,170))