#!/usr/bin/env python
input_list = [26,17,20,11,23,21,13,18, 24,14,12,22,16,15,19,25]
input_list2 = [26,16,15]

def shell_sorting(inp_list):
    """
    Shell sorting
    """
    distance = len(inp_list) // 2
    while distance > 0:
        for i in range(distance, len(inp_list)):
            temp = inp_list[i]
            j_i = i
            while j_i >= distance and inp_list[j_i - distance] > temp:
                print(inp_list)
                inp_list[j_i] = inp_list[j_i - distance]
                j_i = j_i - distance
            inp_list[j_i] = temp
        distance = distance // 2
    return inp_list

print(shell_sorting(input_list2))
