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

def get_how_many_player_at_same_pos(ranked, x):
    occ = 0
    for i in ranked:    
        if i == x :
            occ = occ + 1
    return occ - 1

def map_player_score(ranked):
    #player_score_map = {}
    #for x in ranked:
     #   if player_score_map.get(x):
      #      player_score_map[x] = player_score_map.get(x) + 1
       # else:
        #    player_score_map[x]=  1
    #return player_score_map
    print(list(set(ranked)).sort(reverse=True))
    return list(set(ranked))

def get_new_position(player_position, ranked):
    map_player = sorted(map_player_score(ranked), reverse=True)
    print('map of players : ', map_player)
    i = len(map_player) - 1
    print('map length is : ', i)
    j = i + 1
    print('player position : ',player_position)
    while i > 0:
        #occ = get_how_many_player_at_same_pos(ranked, ranked[i])
        print('map player de i :', map_player[i])
        if player_position == map_player[i]:
            return i + 1
        if player_position < map_player[i]:
            return i +2
        i = i - 1
    return i +1

def climbingLeaderboard(ranked, player):
    # Write your code here
    print(ranked, player)
    position_list = list()
    if validate_player_numbers(len(player), len(ranked)):
        for p in player:
            position_list.append(get_new_position(p, ranked))
    return position_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


def get_new_position(player_position, ranked):
    try:
        i = len(ranked) - 1
        while i > 0:
            if player_position == ranked[i]:
                return i + 1, ranked[0:i]
            if player_position < ranked[i]:
                return i +2, ranked[0:i+1]
            i = i - 1
        return i +1, ranked[0:i+1]
    except Exception as e:
        print('errrrrrrrorororor',e)

        
def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = sorted(list(set(ranked)), reverse=True)
    position_list = list()
    if validate_player_numbers(len(player), len(ranked)):
        for p in player:
            pos , ranked = get_new_position(p, ranked)
            position_list.append(pos)
        return position_list