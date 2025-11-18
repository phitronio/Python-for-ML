if __name__ == '__main__':
    n = int(raw_input().strip())
    integer_list = map(int, raw_input().split())
    print hash(tuple(integer_list))


#it works in python 2