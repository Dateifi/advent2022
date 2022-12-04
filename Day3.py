priorty = 0

with open ("Day3.txt", 'r') as f:
    while True:
        first = f.readline().strip()
        if first == '':
            break
        second = f.readline().strip()
        third = f.readline().strip()
        item = set(first) & set(second) & set(third)
        if list(item)[0].isupper():
            priorty += ord(list(item)[0]) - 38
        else:
            priorty += ord(list(item)[0]) - 96



            # comp1 = line[:len(line)//2]
            # comp2 = line[len(line)//2:]
            # item = set(comp1) & set(comp2)
            # if list(item)[0].isupper():
            #     priorty += ord(list(item)[0]) - 38
            # else:
            #     priorty += ord(list(item)[0]) - 96

print(priorty)