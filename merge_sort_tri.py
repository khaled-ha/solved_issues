
# int_list: list = [45,12,20,7,5,55,40,2,0,80,79,1]
int_list = [5,3,1]

def MergeSort(list):
    if len(list) >1:
    
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        print(f'left before merging and sorting {left}')
        print(f'right before merging and sorting {right}')

        # print('merge sorting left part')
        # print(MergeSort(left))
        MergeSort(left)
        # print(left)
        # print('merge sorting right part')
        MergeSort(right)
        # print(MergeSort(right))
        # print(right)

        a = 0
        b = 0
        c = 0
        print('list : ',list)

        print(f'left part {left}')
        print(f'right part {right}')
        print(a, b ,c , 'pointers')
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a+1
            else:
                list[c] = right[b]
                b = b + 1
            c = c +1
        print(list)
        print('a', a)
        while a < len(left):
            print('in while left part', c)
            list[c] = left[a]
            a = a+1
            c = c+1
        print(list)
        while b < len(right):
            list[c] = right[b]
            b = b+1
            c = c+1
        print(list)
        print('a :', a, 'b: ', b ,'c: ',c)
    print(list)
    return list

if __name__ == '__main__':
    MergeSort(int_list)
    # print(int_list)

