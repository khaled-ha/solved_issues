def get_sum_numbers(x , data, k):
    return [(x,i) for i in data if ((x+i) % k) != 0 ]

def get_nums(data):
    data_set = set()
    for x in data:
        data_set.add(x[0])
        data_set.add(x[1])
    return data_set
    
def nonDivisibleSubset(k, s):
    longest_subset = []
    for i in range(len(s)-2):
        res = get_sum_numbers(s[i], s[i+1:], k)
        if len(res) > len(longest_subset):
            longest_subset = res
    print('this is the longest subset : ', longest_subset)        
    return len(get_nums(longest_subset))