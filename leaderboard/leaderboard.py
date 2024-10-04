#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def validate_player_numbers(n: int, m: int) -> bool:
    if not(1 <= n <= 2 * pow(10,5)):
        raise Exception('number of players is wrong')
    if not (1<= m <= 2 * pow(10, 5)):
        raise Exception('number of ranking is wrong')
    return True

# def get_how_many_player_at_same_pos(ranked, x):
#     occ = 0
#     for i in ranked:    
#         if i == x :
#             occ = occ + 1
#     return occ - 1

# def map_player_score(ranked):
#     #player_score_map = {}
#     #for x in ranked:
#      #   if player_score_map.get(x):
#       #      player_score_map[x] = player_score_map.get(x) + 1
#        # else:
#         #    player_score_map[x]=  1
#     #return player_score_map
#     print(list(set(ranked)).sort(reverse=True))
#     return list(set(ranked))

# def get_new_position(player_position, ranked):
#     map_player = sorted(map_player_score(ranked), reverse=True)
#     print('map of players : ', map_player)
#     i = len(map_player) - 1
#     print('map length is : ', i)
#     j = i + 1
#     print('player position : ',player_position)
#     while i > 0:
#         #occ = get_how_many_player_at_same_pos(ranked, ranked[i])
#         print('map player de i :', map_player[i])
#         if player_position == map_player[i]:
#             return i + 1
#         if player_position < map_player[i]:
#             return i +2
#         i = i - 1
#     return i +1

# def climbingLeaderboard(ranked, player):
#     # Write your code here
#     print(ranked, player)
#     position_list = list()
#     if validate_player_numbers(len(player), len(ranked)):
#         for p in player:
#             position_list.append(get_new_position(p, ranked))
#     return position_list

# def get_new_position_recursed(player_position, ranked):
#     i = len(ranked) - 1
#     if player_position < ranked[i]:
#         return i +2, ranked[:i+1]
#     if player_position == ranked[i]:
#         return i + 1, ranked[:i]
#     get_new_position_recursed(player_position, ranked[:i-1])


# def get_new_position(player_position, ranked):
#     i = len(ranked) - 1
#     while i >= 1:
#         if player_position == ranked[i]:
#             return i + 1, ranked[:i]
#         if player_position < ranked[i]:
#             return i +2, ranked[:i+1]
#         i = i - 1
#     return i +1, ranked[:i+1]

# def get_new_position(player_position, ranked, i):
#     while i>=1:
#         if player_position < ranked[i]:
#             return i +2
#         if player_position == ranked[i]:
#             return i + 1
#         i = i - 1
#     if player_position < ranked[i]:
#         return i +2
#     return i + 1

# def get_new_position(player_position, ranked, i):
#     #print(len(ranked))
#     while i!=0:
#         if player_position < ranked[i]:
#             ranked = ranked[:i+2]
#             return i +2, ranked
#         if player_position == ranked[i]:
#             ranked = ranked[:i+1]
#             return i + 1, ranked
#         i = i - 1
#     if player_position < ranked[i]:
#         ranked = ranked[:i+2]
#         return i +2, ranked
#     if player_position == ranked[i]:
#         ranked = ranked[:i+1]
#         return i + 1, ranked
#     return 1, ranked

def get_new_position(player_position, ranked, i):
    while i!=-1:
        if player_position < ranked[i]:
            ranked = ranked[:i+2]
            return i +2, ranked
        if player_position == ranked[i]:
            ranked = ranked[:i+1]
            return i + 1, ranked
        i -= 1
    return 1, []


#!/bin/python3

import math
import os
import random
import re
import sys


        
def get_new_position(player_position, ranked, i):
    while i!=-1:
        if player_position < ranked[i]:
            #for v in range(i+1, i):
            #    ranked.pop(v)
            return i +2
        if player_position == ranked[i]:
            #for v in range(i+1, i):
            #    ranked.pop(v)
            return i + 1
        ranked.pop(i)
        i -= 1
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())
    ranked = list(set(list(map(int, input().rstrip().split()))))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    ranked = sorted(ranked, reverse=True)
    result = []
    for pl in player:
        new_rank = get_new_position(pl, ranked, i=len(ranked) - 1)
        #ranked = ranked[:new_rank-1]
        result.append(new_rank)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    result = []
    for pl in player:
        new_rank, ranked = get_new_position(pl, ranked, i=len(ranked) - 1)
        result.append(new_rank)
    return result


if __name__ =='__main__':
    #ranked = [997,981,957,933,930,927,926,920,916,896,887,874,863,863,858,847,815,809,803,794,789,785,783,778,764,755,751,740,737,730,691,677,652,650,587,585,583,568,546,541,540,538,531,527,506,493,457,435,430,427,422,422,414,404,400,394,387,384,374,371,369,369,368,365,363,337,336,328,325,316,314,306,282,277,230,227,212,199,179,173,171,168,136,125,124,95,92,88,85,70,68,61,60,59,44,43,28,23,13,12]
    ranked = [997,981,957,933,930,927,926,920,916,896,887,874,863,863,858,847,815,809,803,794,789,785,783,778,764,755,751,740,737,730,691,677,652,650,587,585,583,568,546,541,540,538,531,527,506,493,457,435,430,427,422,422,414,404,400,394,387,384,374,371,369,369,368,365,363,337,336,328,325,316,314,306,282,277,230,227,212,199,179,173,171,168,136,125,124,95,92,88,85,70,68,61,60,59,44,43,28,23,13,12]
    #player_ranking = [12,20,30,32,35,37,63,72,83,85,96,98,98,118,122,125,129,132,140,144,150,164,184,191,194,198,200,220,228,229,229,236,238,246,259,271,276,281,283,287,300,302,306,307,312,318,321,325,341,341,341,344,349,351,354,356,366,369,370,379,380,380,396,405,408,417,423,429,433,435,438,441,442,444,445,445,452,453,465,466,467,468,469,471,475,482,489,491,492,493,498,500,501,504,506,508,523,529,530,539,543,551,552,556,568,569,571,587,591,601,602,606,607,612,614,619,620,623,625,625,627,638,645,653,661,662,669,670,676,684,689,690,709,709,710,716,724,726,730,731,733,737,744,744,747,757,764,765,765,772,773,774,777,787,794,796,797,802,805,811,814,819,819,829,830,841,842,847,857,857,859,860,866,872,879,882,895,900,900,903,905,915,918,918,922,925,927,928,929,931,934,937,955,960,966,974,982,988,996,996]
    player_ranking = [12,20,30,32,35,37,63,72,83,85,96,98,98,118,122,125,129,132,140,144,150,164,184,191,194,198,200,220,228,229,229,236,238,246,259,271,276,281,283,287,300,302,306,307,312,318,321,325,341,341,341,344,349,351,354,356,366,369,370,379,380,380,396,405,408,417,423,429,433,435,438,441,442,444,445,445,452,453,465,466,467,468,469,471,475,482,489,491,492,493,498,500,501,504,506,508,523,529,530,539,543,551,552,556,568,569,571,587,591,601,602,606,607,612,614,619,620,623,625,625,627,638,645,653,661,662,669,670,676,684,689,690,709,709,710,716,724,726,730,731,733,737,744,744,747,757,764,765,765,772,773,774,777,787,794,796,797,802,805,811,814,819,819,829,830,841,842,847,857,857,859,860,866,872,879,882,895,900,900,903,905,915,918,918,922,925,927,928,929,931,934,937,955,960,966,974,982,988,996,996]
    output = [97,
96,
94,
94,
94,
94,
89,
87,
87,
86,
83,
83,
83,
83,
83,
81,
81,
81,
80,
80,
80,
80,
76,
76,
76,
76,
75,
74,
73,
73,
73,
72,
72,
72,
72,
72,
72,
71,
70,
70,
70,
70,
69,
69,
69,
67,
67,
66,
63,
63,
63,
63,
63,
63,
63,
63,
61,
59,
59,
57,
57,
57,
54,
52,
52,
51,
50,
49,
48,
47,
47,
47,
47,
47,
47,
47,
47,
47,
46,
46,
46,
46,
46,
46,
46,
46,
46,
46,
46,
45,
45,
45,
45,
45,
44,
44,
44,
43,
43,
41,
39,
38,
38,
38,
37,
37,
37,
34,
34,
34,
34,
34,
34,
34,
34,
34,
34,
34,
34,
34,
34,
34,
34,
32,
32,
32,
32,
32,
32,
31,
31,
31,
30,
30,
30,
30,
30,
30,
29,
29,
29,
28,
27,
27,
27,
25,
24,
24,
24,
24,
24,
24,
24,
21,
19,
19,
19,
19,
18,
17,
17,
16,
16,
16,
16,
16,
16,
15,
15,
15,
14,
14,
13,
13,
12,
12,
11,
10,
10,
10,
10,
10,
9,
9,
8,
8,
6,
6,
6,
5,
4,
4,
4,
3,
3,
3,
2,
2,
2,
2]
    print(climbingLeaderboard(ranked, player_ranking))