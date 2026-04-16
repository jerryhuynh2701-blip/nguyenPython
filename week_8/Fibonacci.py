def fib(n):
    arr = []
    if n >= 0:
        arr.append(0)
    if n >= 1:
        arr.append(1)
    

    for i in range(2,n+1):
        arr.append(arr[i-1]+arr[i-2])
    
    print(arr)

fib(6)

# def fib(n):
#     arr = [0] * (n + 1)
#     arr[1] = 1

#     for i in range (2,n+1):
#         arr[i] = arr[i-1] + arr[i-2]
    
#     return arr[n]


# print(fib(0))