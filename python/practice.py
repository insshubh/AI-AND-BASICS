from love_Calc import check

"""
def highest_even(li):
    high = -1
    for i in li:
        if i % 2 == 0:
            high = max(i,   high)
    return high


print(highest_even([1, 2, 5, 6, 18, 10]))
"""

# Printing star Pattern
#           *
#         * * *
#       * * * * *

"""
inp = int(input("Enter the number"))
for i in range(0, inp):
    for j in range(0, inp - i - 1):
        print(" ",end=' ')
    for k in range(0, 2*i + 1):
        print('*', end=' ')
    print()
"""

# Sort an Array using any Sorting Algo
# BubbleSort->Assembly Line big val last me
"""
def sort_bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n - 1-i):
            if arr[j+1] <= arr[j]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

"""


def print_arr(ar):
    n = len(ar)
    for i in range(0, n):
        print(ar[i])


arr = [11, 3, 40, 5, 5, 7, 7]

# SelectionSort-> Find the minimumVal index then swap it

"""
def selection_sort(ar):
    n = len(arr)
    for i in range(0, n - 1):
        index = i
        for j in range(i, n):
            if arr[j] < arr[index]:
                index = j
        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp

"""

# selection_sort(arr)
# print_arr(arr)

if __name__ == "__main__":
    check(30)
