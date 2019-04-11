import random
import sys

def goal(rawList, newList):
    # sorted(rawList)
    rawList.sort()
    return newList == rawList[::-1]


"""pos = start of allowed new array"""


def flip(arr, arraySize=0):
    if len(arr) <= 1:
        return arr
    indexOfMaxValue = arr.index(max(arr[arraySize:]), arraySize, len(arr))
    tmp_list = arr[indexOfMaxValue:]
    out_arr = arr[arraySize:indexOfMaxValue] + tmp_list[::-1]
    final_arr = arr[:arraySize] + out_arr[::-1]
    if not goal(arr, final_arr):
        return flip(final_arr, arraySize + 1)

    return final_arr


######## TESTING ########


rand_from = 1
rand_till = 5230
anz_rekursionen = 10000
sys.setrecursionlimit(anz_rekursionen-1)
number_Of_Pancake = rand_till - 1

myList = random.sample(range(rand_from, rand_till), number_Of_Pancake)

# change = myList[5:]
# print(change)
# print(change.index(max(change)))


results = (flip(myList))

for result in results:
    print(result)

########
