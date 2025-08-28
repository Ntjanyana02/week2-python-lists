#!/usr/bin/env python3
"""
Week Two Assignment: List operations

Steps:
1) Create an empty list called my_list.
2) Append 10, 20, 30, 40 (individually).
3) Insert 15 at the second position (index 1).
4) Extend with [50, 60, 70].
5) Remove the last element.
6) Sort ascending.
7) Find and print the index of value 30.
"""

def main() -> None:
    # 1) Create empty list
    my_list = []

    # 2) Append elements one by one
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    # 3) Insert 15 at second position (index 1)
    my_list.insert(1, 15)

    # 4) Extend with another list
    my_list.extend([50, 60, 70])

    # 5) Remove the last element
    my_list.pop()

    # 6) Sort in ascending order
    my_list.sort()

    # 7) Find index of 30 and print results
    index_30 = my_list.index(30)

    print("my_list:", my_list)       # Expected: [10, 15, 20, 30, 40, 50, 60]
    print("Index of 30:", index_30)  # Expected: 3 (0-based)

if __name__ == "__main__":
    main()
