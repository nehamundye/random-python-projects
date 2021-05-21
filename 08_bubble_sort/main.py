def bubble_sort(arr):
    for j in range(len(l)-1):
        swapped = False
        for i in range(0, len(l)-j-1):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
                swapped = True
        if swapped == False:
            break
    return arr


l = [10, 1, 2, 50, 70, 7, 5, 9, 28]
print(f"Sorted Array : {bubble_sort(l)}")


