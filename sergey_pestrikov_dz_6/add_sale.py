def enter(argv):
    program, *arg = argv
    arg_st = ','.join(arg)
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{arg_st}\n')



if __name__ == '__main__':
    import sys
    exit(enter(sys.argv))
