array = [5,6,1,9,7,3,33,14,2,3,8,44,20,10,4]
input_list = [26,17,20,11,23,21,13,18, 24,14,12,22,16,15,19,25]

def shell_sorting(array):
    """
    shell sort
    """
    step = len(array) // 2
    while step > 0:
        print(step)
        for i in range(step, len(array)):
            val = array[i]
            j = i
            while j >= step and array[j - step] > val:
                array[j] = array[j - step]
                j = j - step
            array[j] = val
        print(array)
        step = step // 2
    return array

if __name__ == "__main__":
    res = shell_sorting(input_list)
