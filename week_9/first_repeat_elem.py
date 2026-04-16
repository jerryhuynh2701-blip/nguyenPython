def helper(arr):
    cache = {}
    for k, v in enumerate(arr):
        if v in cache:
            return cache[v]
        cache[v] = k    
    print(cache)

arr = [1, 5, 3, 4, 3, 5, 6]

helper(arr)
