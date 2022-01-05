
dictionary = {
    "a": {
        "1": 1,
        "2": 2,
        "3": 3,
    },
    "b": {
        "1": 4,
        "2": 5,
        "3": 0,
    },
    "c": {
        "1": 7,
        "2": 8,
        "3": 0,
    },
    "d": {
        "1": 10,
        "2": 11,
        "3": 0,
    },
}

for i in range(len(dictionary)):
    print(dictionary.popitem()[1]["1"])
    # print(dictionary.popitem()[1])