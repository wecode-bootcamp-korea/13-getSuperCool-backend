from parameter import trace

@trace
def add(a,b):
    return a+b

print(add(10,20))