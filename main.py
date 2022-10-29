def str():
    try:
        str = input("str - ")
        rts = (str[::-1])
        if str == rts:
            print('Слово',str,'є паліндромом')
        else:
            print('Слово', str, 'не є паліндромом')
    except Exception as ex:
        print(f'Eror information: {ex}')


str()