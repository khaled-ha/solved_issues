

data_list = [5,4,9,3,1,0,15,11,10,8,7,2]

def merge_sort(data): 
    if len(data)>1:
        left_side = data[:len(data)//2]
        right_side = data[len(data)//2+1:]

        merge_sort(left_side)
        merge_sort(right_side)
        

        a = 0
        b = 0
        c = 0

        while a < len(left_side) and b < len(right_side):
            if left_side[a] < right_side[b]:
                data[c] = left_side[a]
                a += 1
            else:
                data[c] = right_side[b]
                b+=1
            c +=1
            while a < len(left_side):
                data[c] = left_side[a]
                a += 1
                c += 1
            while b < len(right_side):
                data[c] = right_side[b]
                b += 1
                c += 1
        return data

    return data