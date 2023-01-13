
# int_elements: elements = [45,12,20,7,5,55,40,2,0,80,79,1]
int_elements = [4,1,3,2]

def MergeSort(elements):
    if len(elements) >1:
    
        mid = len(elements)//2
        left = elements[:mid]
        right = elements[mid:]
        left = MergeSort(left)
        right = MergeSort(right)
 
        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                elements[c] = left[a]
                a = a+1
            else:
                elements[c] = right[b]
                b = b + 1
            c = c +1
        while a < len(left):
            elements[c] = left[a]
            a = a+1
            c = c+1
        while b < len(right):
            elements[c] = right[b]
            b = b+1
            c = c+1
    return elements

if __name__ == '__main__':
    print(MergeSort(int_elements))
    # print(int_elements)

