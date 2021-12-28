
class class1:
    def decorator(func):
        print(func.__name__)
        def wrapper(arg1):
            print('전처리')   
            func(arg1)
            print('후처리')
        return wrapper

    @decorator
    def example1(arg1):
        print(arg1,"example1함수출력")

class1.example1("asd")