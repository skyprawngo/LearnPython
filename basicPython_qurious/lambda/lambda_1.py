dictionary = [
    {
        "1": 1,
        "2": 5,
        "3": 8,
    },
    {
        "1": 2,
        "2": 3,
        "3": 6,
    },
    {
        "1": 1,
        "2": 9,
        "3": 0,
    },
    {
        "1": 10,
        "2": 2,
        "3": 7,
    },
]

print(dictionary.sort(key=lambda x: x["2"] ))
print(dictionary)