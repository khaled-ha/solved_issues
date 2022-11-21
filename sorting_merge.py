

data_list = [5,4,9,3,1,0,15,11,10,8,7,2]

def merge_sort(data):
    if len(data) <= 2:
        return data
    
    left_side = data[:len(data)//2]
    right_side = data[len(data)//2+1:]
    
    if len(left_side) > 2:
        merge_sort(left_side)
    
                  
    