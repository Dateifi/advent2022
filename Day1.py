import operator


def read_file():
    cal_list = {}
    with open('Day1.txt', 'r') as f:
        try:
            i=0
            for line in f:
                if line.startswith('\n'):
                    i+=1
                else:
                    cal_list[i] = cal_list.get(i, 0) + int(line)
        except:
            pass
    return cal_list

def find_top_three(cal_list):
    top_three = sorted(cal_list.items(), key=operator.itemgetter(1), reverse=True)[:3]
    return sum([x[1] for x in top_three])


def main():
    cal_list = read_file()
    #print(cal_list[max(cal_list.items(), key=operator.itemgetter(1))[0]])
    print(find_top_three(cal_list))

main()