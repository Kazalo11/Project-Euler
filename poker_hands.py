player_1 = []
player_2 = []
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
one_pair = 2
two_pair = 3
three_kind = 4
straight_points = 5
flush_points = 6
full_house = 7
four_kind = 8
straight_flush = 9
royal_flush = 10


def find_order(x):
    return order.index(x[0])


def player_1_tie(x, y):
    for i in range(len(x)):
        if find_order(x[i]) < find_order(y[i]):
            return True
        elif find_order(x[i]) > find_order(y[i]):
            return False


with open('p054_poker.txt') as f:
    for game in f:
        game = game.rstrip().split(" ")
        player_1_hand = game[0:len(game) // 2]
        player_2_hand = game[len(game) // 2:len(game)]
        player_1_hand = sorted(player_1_hand, key=find_order)
        player_2_hand = sorted(player_2_hand, key=find_order)
        player_1.append(player_1_hand)
        player_2.append(player_2_hand)


def flush(items):
    possible_royal = False
    temp = 0
    if all(x[1] == items[0][1] for x in items):
        if items[0][0] == "A":
            possible_royal = True
        temp = order.index(items[0][0])
        for i in range(1, len(items)):
            if order.index(items[i][0]) == temp + 1:
                temp = order.index(items[i][0])
            else:
                return flush_points
        if possible_royal:
            return royal_flush
        else:
            return straight_flush
    else:
        return 0


def straight(items):
    temp = order.index(items[0][0])
    for i in range(1, len(items)):
        if order.index(items[i][0]) == temp + 1:
            temp = order.index(items[i][0])
        else:
            return 0
    return straight_points


def same_kind(items):
    frequency = {}
    for item in items:
        frequency[item[0]] = frequency[item[0]] + 1 if item[0] in frequency else 1


    frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1],reverse=True)}
    biggest = list(frequency.values())[0]
    if biggest == 4:
        return (four_kind,frequency)
    elif biggest == 3:
        if list(frequency.values())[1] == 2:
            return (full_house,frequency)
        return (three_kind,frequency)
    elif biggest == 2:
        count = 0
        for key, value in frequency.items():
            if value == biggest:
                count += 1
        if count == 1:
            return (one_pair,frequency)
        elif count == 2:
            return (two_pair,frequency)
    else:
        return (0,0)


winner_1 = 0
winner_2 = 0
temp_1 = 0
temp_2 = 0

for i in range(len(player_1)):
    hand_1 = player_1[i]
    hand_2 = player_2[i]
    temp_1 = max(flush(hand_1), straight(hand_1), same_kind(hand_1)[0])
    temp_2 = max(flush(hand_2), straight(hand_2), same_kind(hand_2)[0])
    print(f'Player 1 score: {temp_1}, Player 2 score: {temp_2}')
    if temp_1 > temp_2:
        winner_1 += 1
    elif temp_1 == temp_2:
        if (temp_1 in [2,3,4,7,8]):
            compare_1 = same_kind(hand_1)[1]
            compare_2 = same_kind(hand_2)[1]
            for (k1,v1), (k2,v2) in zip(compare_1.items(),compare_2.items()):
                if order.index(k1) < order.index(k2):
                    winner_1+=1
                    break
                elif order.index(k2) < order.index(k1):
                    winner_2+=1
                    break
        else:
            if player_1_tie(player_1[i], player_2[i]):
                print("Player 1 wins!")
                winner_1 += 1
            else:
                winner_2 += 1
    else:
        winner_2 += 1

print(winner_1)
