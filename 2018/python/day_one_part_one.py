def add(list):
    sum = 0
    for elem in list:
        sum += int(elem)
    return sum

def main():
    f = open('input.txt', 'r')
    lines = f.readlines()
    result = add(lines)
    print(result)

if __name__ == '__main__':
    main()
