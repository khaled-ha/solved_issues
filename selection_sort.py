input_list = [26,17,20,11,23,21,13,18, 24,14,12,22,16,15,19,25]


def slection_tri(input_list):
    """
    Selection Tri
    """
    last_pos = len(input_list)-1
    while last_pos > 0:
        for i in range(0, last_pos -1):
            if input_list[i] > input_list[last_pos]:
                input_list[last_pos] ,input_list[i] = input_list[i], input_list[last_pos]
        last_pos -= 1
    return input_list


if __name__ == '__main__':
    res = slection_tri(input_list)
    print(res)
