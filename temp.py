list1 = [1, 2, 3, 4, 5, 9, 9, 8, 9, 6, 7]


# def sorting(listx):
#     sorted_list = []
#     while(len(listx) != 0):
#         max2 = max(listx)
#         for i in listx:
#             if i == max2:
#                 sorted_list.append(i)
#         listx = [i for i in listx if i != max2]
#     return sorted_list

# print(sorting(list1))



def sec_max(listx):
    if len(listx) < 2:
        return None
    max1 = listx[0]
    max2 = listx[1]
    for i in range(len(listx) - 1):
        if max1 < listx[i+1]:
            max1, max2 = listx[i+1], max1
        elif max2 < listx[i+1]:
            max2 = listx[i+1]
        elif max1 == max2:
            max2 = listx[i+1]

    if max1 == max2:
        return None
    return max2        
    
print(sec_max([6, 6,7]))