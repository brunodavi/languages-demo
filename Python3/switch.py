def dict_case_func(key):
    dict_case = {
        'one': lambda: print(str(key).upper()),
        'two': lambda: print(str(key).lower()),
        'three': lambda: print(str(key).title()),
    }

    dict_case.get(key, lambda: print(key))()

dict_case_func('Two')


# match case python3.10

key = 'one'

match key:
    case 'one':
        print(key.upper())
        pass

    case 'two':
        print(key.lower())
        pass

    case 'three':
        print(key.title())
        pass
