def list2D_to_1D_list(list):
    result = []
    for row in list:
        for item in row:
            result.append(item)

    return result

print(list2D_to_1D_list([[1,2,3],[2,3]]))

