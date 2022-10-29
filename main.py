def str():
    try:
        text = input('text - ')
        res = text.count('.') + text.count('?') + text.count('!')
        print(res)
    except Exception as ex:
        print(f'Eror information: {ex}')


str()