
def logger(func):
    def wrapper(*args,**kwargs):
        #print("Inside Wrapper Function")
        result =func(*args,**kwargs)
        return result
    return wrapper



@logger
def calculate_sum(a ,b,c):
    return a+b+c

print(calculate_sum(5, 6,1))
