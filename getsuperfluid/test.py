def trace(func):
    def wrapper():
        print(func.__name__, "함수시작")
        func()
        print(func.__name__, "함수 끝")
        
    return wrapper

@trace
def hello():
    print('hello')
@trace
def world():
    print('world')


hello()
world()

