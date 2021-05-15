"""
Execution time difference between binary search and naive search

Binary Search:
    1. Compare search_number with the middle element.
    2. If search_number matches with the middle element, we return the mid index.
    3. Else if search_number is greater than the mid element, then search_number can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
    4. Else if search_number is smaller, the search_number must lie in the left (lower) half. So we apply the algorithm for the left half.
"""

import random
import math
import time


# create a list of random numbers.
random.seed(30)
number_list = random.sample(range(0, 10000), 7000)
number_list.sort()


search_number = 600

# Naive search
def naive_search():
    for i in range(0, len(number_list)-1):
        if search_number == number_list[i]:
            return f"Naive Search: Found the search_number {search_number} at index: {i}"
    return f"Naive Search: Search number {search_number} not found."



# Binary search
def binary_search(low_index, middle_index, high_index):

    if search_number == number_list[middle_index]:
        print(f"Binary Search: Found the search_number {search_number} is at index: {middle_index}")

    else:   
        while (low_index != middle_index) and (high_index != middle_index):
            if search_number == number_list[middle_index]:
                print(f"Binary Search: Found the search_number {search_number} is at index: {middle_index}")
                break

            elif search_number > number_list[middle_index]:
                low_index = middle_index + 1
                high_index = len(number_list) - 1
                middle_index = math.ceil((high_index - low_index)/2) + low_index
            
            elif search_number < number_list[middle_index]:
                low_index = low_index
                high_index = middle_index - 1
                middle_index = math.ceil((high_index - low_index)/2) + low_index


    if (low_index == middle_index) or (high_index == middle_index):
        if search_number == number_list[middle_index]:
            print(f"Binary Search: Found the search_number {search_number} at index: {middle_index}")
        elif search_number == number_list[low_index]:
            print(f"Binary Search: Found the search_number {search_number} at index: {low_index}")
        else:
            print(f"Binary Search: Search number {search_number} not found.")

    print(f"Binary Search execution time: {(time.time() - start_time_binary)} seconds")




if __name__ == '__main__':

    # print(number_list)
    
    # Naive search execution time
    start_time_naive = time.time()
    print(naive_search())
    print(f"Naive Search execution time: {(time.time() - start_time_naive)} seconds")



    print("\r")
    # Binary search execution time
    start_time_binary = time.time()
    low_index = 0
    middle_index = math.ceil(len(number_list)/2)
    high_index = len(number_list) - 1 
    
    binary_search(low_index, middle_index, high_index)