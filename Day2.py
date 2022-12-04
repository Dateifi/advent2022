# oppo = {'A': 1, 'B': 2, 'C': 3}
# me = {'X': 1, 'Y': 2, 'Z': 3}
# counter = {1: 2, 2: 3, 3: 1}
#
# total = 0
#
# with open ('Day2.txt', 'r') as f:
#     for line in f:
#         game = line.split()
#         if oppo[game[0]] == me[game[1]]:
#             total = total + 3 + me[game[1]]
#         elif me[game[1]] == counter[oppo[game[0]]]:
#             total = total + 6 + me[game[1]]
#         else:
#             total = total + me[game[1]]
#
# print(total)


oppo = {'A': 1, 'B': 2, 'C': 3}
me = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
counter = {1: 2, 2: 3, 3: 1}

total = 0

with open ('Day2.txt', 'r') as f:
    for line in f:
        game = line.split()
        if game[1] == 'X':
            for k,v in counter.items():
                if v == oppo[game[0]]:
                    total = total + 0 + k
        elif game[1] == 'Y':
            total = total + 3 + oppo[game[0]]
        else:
            total = total + 6 + counter[oppo[game[0]]]

print(total)

