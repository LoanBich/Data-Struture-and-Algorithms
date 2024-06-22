# Ex3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

def sortedTwoArray(arr1, arr2):
    i = j = 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.extend([arr1[i], arr2[j]])
        else:
            ans.extend([arr2[j], arr1[i]])
        i += 1
        j += 1

    ans.extend(arr1[i::])
    ans.extend(arr2[j::])
   
    return ans

print(sortedTwoArray([1,1,4,5,9], [0,1,4,5,9,10,12]))