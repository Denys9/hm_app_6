def str():
    try:
        text = input('text - ')
        wordsText = input('word - ')
        words = wordsText.split()
        for word in words:
            if text.count(word)>0:
                origen = word
                temp = word[0].upper()+word[1:]
                text = text.replace(origen, temp)
                print(text)
    except Exception as ex:
        print(f'Eror information: {ex}')


str()