def f():
    names = [
        "maneskin",
        "21 pilots",
        "harry styles",
        "pink",
        "sting",
        "metallica",
        "pink floyd",
        "wham"
    ]

    del names[3]
    del names[4]

    return names

print(f())