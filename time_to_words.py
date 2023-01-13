special_minutes_map = {
    15: 'quarter',
    30: 'half',
    45: 'quarter',
}

basic_hour_map = {
    2: 'twenty',
}

int_map = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'quarter',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nighteen',
    20:'twenty',
}

def convert_minutes(m):
    if m in [15, 30, 45]:
        return special_minutes_map[m]
    if m > 30:
        m = 60 -m 
    if m > 20:
        a,b = divmod(m, 10)
        return basic_hour_map[a] + ' ' + int_map[b] + ' minutes'
    else:
        if m == 1:
            return int_map[m] + ' minute'
        return int_map[m] + ' minutes'

def timeInWords(h, m):
    hour = int_map[h]
    if m == 0:
        return hour + " o\' clock"
    minute = convert_minutes(m)
    if m > 30:
        return minute + ' to ' + int_map[h+1]
    return minute + ' past ' + hour