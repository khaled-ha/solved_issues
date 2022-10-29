# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from functools import reduce
from collections import defaultdict

    
def get_all_occured_sequence(card_num):
    occ_map = defaultdict(lambda: 1)
    occ_list = []
    for i in range(1, len(card_num)):
        if card_num[i] == card_num[i-1]:
            occ_map[card_num[i]] += 1
        else:
            occ_list.append(
                (
                    card_num[i-1], 
                    occ_map[card_num[i-1]]
                ))
    if not all(list(map(lambda x : x[1] < 4, [x for x in occ_list]))):
        return False
    return True
               
def check_all_4_combination(data):
    return all(list(map(lambda x : len(x) == 4, data))) and len(data) == 4
    
def check_card_num_length(card_num):
    if '-' in str(card_num):
        if not check_all_4_combination(card_num.split('-')):
            return False
    else:
        if len(str(card_num)) > 16:
            return False
    return True

def check_allowed_digit_and_special_caracter(card_num):
    if not all(map(lambda x :  x in ['0','1','2','3','4','5','6','7','8','9','-'],[x for x in card_num])):
        return False
    if not all(map(lambda x :  x in ['4','5','6'],[x for x in card_num[0]])):
        return False
    return True

def validate_card_number(card_num):
    if not check_card_num_length(card_num):
        return 'Invalid'
    if not check_allowed_digit_and_special_caracter(card_num):
       return 'Invalid'
    #print('--------',get_all_occured_sequence(card_num.replace('-', '')))
    if not get_all_occured_sequence(card_num.replace('-', '')):
        return 'Invalid'
    return 'Valid'
    
data = [x for x in sys.stdin]
for x in data[1:]:
    #data = ['3695-7963-915827-75', '3143-4672-8798-2968-2968', '6444-4444-4444-4918','6865396515642918', '6865396515642','4695-7963-9778-2775']
    #print([get_all_occured_sequence(x) for x in data])
    print(validate_card_number(x.replace('\n', '')))