# Enter your code here. Read input from STDIN. Print output to STDOUT
from functools import reduce
import sys

def get_happiness():
    data = [line.replace('\n', '') for line in sys.stdin.readlines()]
    array = data[1].split(' ')
    A = data[2].split(' ')
    B = data[3].split(' ')
    
    happines_value = 0
    intersection = set(A).intersection(set(B))
    A, B = set(A) - intersection, set(B) - intersection
    
    for x in array:
        if str(x) in A:
            happines_value += 1
        if str(x) in B:
            happines_value -= 1
    return happines_value
        
    
if __name__ == '__main__':
    print(get_happiness(), file=sys.stdout)
