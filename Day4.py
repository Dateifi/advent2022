import re
counter = 0
with open ("Day4.txt", "r") as f:
    for line in f:
        pairs = re.split(r'[-;,]', line)
        if not set((range(int(pairs[0]),int(pairs[1])+1))).isdisjoint(range(int(pairs[2]),int(pairs[3])+1)) or not set((range(int(pairs[2]),int(pairs[3])+1))).isdisjoint(range(int(pairs[0]),int(pairs[1])+1)):
            counter += 1
print(counter)