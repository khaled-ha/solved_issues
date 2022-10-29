# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from functools import reduce
from collections import defaultdict

    
def get_all_occured_sequence(card_num):
    occ_map = defaultdict(lambda: 0)
    occ_list = []
    for i in range(1, len(card_num)):
        if card_num[i] == card_num[i-1]:
            occ_map[card_num[i]] += 1
        else:
            occ_map[card_num[i-1]] += 1
            occ_list.append(
                (
                    card_num[i-1], 
                    occ_map[card_num[i-1]]
                ))
            occ_map.clear()
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
        if len(str(card_num)) != 16:
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
    print('--------',get_all_occured_sequence(card_num.replace('-', '')))
    if not get_all_occured_sequence(card_num.replace('-', '')):
        return 'Invalid'
    return 'Valid'
    
#data = [x for x in sys.stdin]
#for x in data[1:]:
    #data = ['3695-7963-915827-75', '3143-4672-8798-2968-2968', '6444-4444-4444-4918','6865396515642918', '6865396515642','4695-7963-9778-2775']
    #print([get_all_occured_sequence(x) for x in data])
 #   print(validate_card_number(x.replace('\n', '')))

if __name__ == '__main__':
    data = ['3695-7963-915827-75', '3143-4672-8798-2968-2968', '6444-4444-4444-4918','6865396515642918', '6865396515642','4695-7963-9778-2775']
    data2 = ['1182387522195848','4898285859544556','3533946521218854','2178579985193175','9691928949545344','1327576477684519','6885867822596993','1958129523778579','2357676157819124','9832746248713726','3673159777236652','8626186974574971','9687622296992497','6731749895254584','8231635922318254','7728878259735616','3347275338764373','6624557432269847','3164653818478977','7683817293887423','4654491168789767','6942469919536219','8434524674271379','6619249165433473','8842787232483367','5349898497837349','4841565975496529','7635659522159832','6699889899699968','5274676861386577','7261479482325831','9855821811363989','5462941623272486','2168457338741692','3493828267535654','7688277563695358','4621162653647299','5588937472734175','6313634439334582','2621731928824298','9356326214767474','6399396262113367','7326622854597675','2179646384144599','8723731421194264','9893925198222769','8493394862176119','9182146786584817','7865278423923993','5437343432579992']
    data3 = ['6699889899699968']
    for x in data3 :
        print(validate_card_number(x))

#wrong one 6699889899699968
#Invalid    Invalid
#Valid    Valid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Valid    Valid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Valid    Valid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Valid    Valid
#Invalid    Invalid
#Invalid    Invalid
#Valid    Valid
#Valid    Valid
#Invalid    Invalid
#Valid    Valid
#Invalid    Invalid
#Valid    Valid
#Valid    Valid
#Invalid    Invalid

#Valid    Invalid

#Valid    Valid
#Invalid    Invalid
#Invalid    Invalid
#Valid    Valid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Valid    Valid
#Valid    Valid
#Valid    Valid
#Invalid    Invalid
#Invalid    Invalid
#Valid    Valid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Invalid    Invalid
#Valid    Valid