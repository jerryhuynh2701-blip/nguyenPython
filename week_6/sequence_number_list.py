def dummy(arr):
    for i in range(len(arr)- 2):
        if arr[i] == 1 and arr[i+1] == 2 and arr[i+2] == 3:
            return True
    return False

print(dummy([1,3,6,1,3,9]))






