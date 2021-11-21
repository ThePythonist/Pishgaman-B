def f():
    numbers = []
    data = [
        "Python",
        12,
        13.5,
        [()],
        {"city":"new york"},
        7
    ]

    for item in data :
        # if type(item) == int or type(item) == float :
        if type(item) in [int, float] :
            numbers.append(item)


    return numbers


print(f())