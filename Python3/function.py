def func(a, b: float, c = 8, *d, **e):
    print(a)

    print(b)

    print(c)

    print(d[3])

    print(e['t'], e['f'], sep='\n')

func(
    # a
    'text',

    # b
    5.2,

    # c
    10,

    # d
    1,
    2,
    3,
    4,
    5,

    # e
    t=True,
    f=False
)
