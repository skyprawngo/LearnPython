
class class1:
    def decorator(func):
        print(func.__name__)
        def wrapper():
            print('전처리')   
            func()
            print('후처리')
        return wrapper

    @decorator
    def example1():
        print("example1함수출력")

class1.example1()