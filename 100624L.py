# Insertion sort

# Input: A squence of n numbers (a1...an)
# Output: A permutation (a1'...an') s.t. a1'<=...<=an'

import random
import copy
from typing import List

def main():
    list_length = 100 # Edit this for different sized random lists
    num_size = 100 # Edit this to control the maximum distance from 0 that any nubmer can be

    sort_list = []
    
    for i in range(list_length):
        sort_list.append(random.randint(-num_size,num_size))

    print("List is:")
    print(sort_list)
    new_sort_list = sort(copy.deepcopy(sort_list))
    print("Sorted list is:")
    print(new_sort_list)
    if sort_list == new_sort_list:
        print("Lists are the same!")
    if len(sort_list) != len(new_sort_list):
        print("Lists are not the same size!")
        if len(sort_list) > len(new_sort_list):
            print("New list has lost values")
        else:
            print("New list has duplicated values")
    if not sorted(new_sort_list):
        print("New list not sorted!")
    if sorted(sort_list):
        print("Input list is already sorted!")

def sort(sort_list: List[int]) -> List[int]:
    invariant_list = copy.deepcopy(sort_list)
    new_list = [sort_list.pop(0)]
    for i in sort_list:
        for j in range(len(new_list)):
            if new_list[j] > i:
                new_list.insert(j, i)
                break
            if j == len(new_list) - 1:
                new_list.append(i)
        if not loop_invariant(invariant_list, new_list):
            print("Invariant broken. Algorithm incorrectly implemented")
    return new_list

def sorted(sort_list: List[int]) -> bool:
    for i in range(len(sort_list)):
        if i < len(sort_list) - 1 and sort_list[i] > sort_list[i + 1]:
            return False
    return True

def loop_invariant(initial_list, sorted_list):
    # This is mostly pointless; just an exercise in conceptualizing invariants in code

    # Loop invariants:
    # Sorted list consists of elements 1-n of initial list
    # Sorted list is in sorted order
    if not sorted(sorted_list):
        return False
    for i in initial_list[:len(sorted_list)]:
        if i not in sorted_list:
            return False
    return True



if __name__ == "__main__":
    main()