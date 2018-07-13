def insertionsort(lists): # Sort the list using insertion sort.
    steps = 0
    for item in lists:
        j = lists.index(item)
        while j > 0:
            if lists[j - 1] > lists[j]:
                lists[j-1],lists[j] = lists[j],lists[j-1] # Swaps the values for sorting
            else:
                break
            j = j - 1
            steps += 1
    print(lists)
    print("Steps taken to sort the given list: " + str(steps))
numbers = [1,4,3,5,0,2,7,6,9,8,10]
insertionsort(numbers)
