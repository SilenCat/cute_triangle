while True:
    option = input('> ')
    if option.lower() == 'q' or option.lower() == '':
        print('Quit!')
        break
    i0 = i1 = int(option)
    j = 0
    k = 0
    while i1 > 0:
        k += 1
        if i0 == j/2 + 1:
            for count in range(j + 1):
                print('*', end='')
            print('\n')
            break
        if k == i1:
            k = 0
            j += 2
            i1 += 1
            print('*')
            continue
        if k == i1 - j:
            print('*', end='')
        else:
            print(' ', end='')
