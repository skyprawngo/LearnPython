import pprint
a = {
    "a": {
        1: 10,    
        2: 20,   
        3: 30,  
        4: 40
    },
    "b": 2,
    "c": 3,
    "d": 4
}

class b:
    def c():
        global a
        pprint.pprint(a)
        a = ["123"]
        

b.c()
print(a)
