input_list = [26,17,20,11,23,21,13,18, 24,14,12,22,16,15,19,25]
input_list2 = [26,16,15]

def shell_sorting(inp_list):
    distance = len(inp_list) // 2
    # print(distance)
    while distance > 0:
        # if distance == 1:
        for i in range(distance, len(inp_list)):
            temp = inp_list[i]
            ji = i
            while ji >= distance and inp_list[ji - distance] > temp:
                # if distance == 1:
                    # import ipdb;ipdb.set_trace()
                print(inp_list)
                inp_list[ji] = inp_list[ji - distance]
                ji = ji - distance
            inp_list[ji] = temp
        distance = distance // 2
        # print(distance)
    return inp_list

print(shell_sorting(input_list2))