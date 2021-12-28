
class class1:
    cls_arg1 = "123"
    def decorator(func):
        def wrapper(arg1):
            print(class1.cls_arg1)
            print('전처리')   
            func(arg1)
            print('후처리')
        return wrapper

    @decorator
    def example1(arg1):
        print(f"{arg1},{class1.cls_arg1},esample1함수출력")

instance1 = class1
instance1.example1("abc")