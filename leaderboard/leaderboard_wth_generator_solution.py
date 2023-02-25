# def get_new_position(player_position, ranked):
#     i = len(ranked) - 1
#     while i >= 1:
#         if player_position < ranked[i]:
#             yield i +2
#         if player_position == ranked[i]:
#             yield i + 1
#         i = i - 1
#     yield i +1

def get_new_position(player_position, ranked, i):
    print('start')
    while i>=1:
        if player_position < ranked[i]:
            return i +2
        if player_position == ranked[i]:
            return i + 1
        i = i - 1
    print(i)
    return i +1
def get_player_leaderborad(ranked, player):
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    return [get_new_position(p, ranked) for p in player]


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(set(list(map(int, input().rstrip().split()))))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    ranked.sort(reverse=True)
    #ranked = sorted(ranked, reverse=True)
    result =[next(get_new_position(p, ranked)) for p in player]