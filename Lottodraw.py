import random



def repeat(func):
    def wrapper(*args):
        func(*args)
        func(*args)
    return wrapper


@repeat
def lottodraw(start,end):
    random_number=random.randint(start,end)
    print(f"Randomly Drawn Number {random_number}")

lottodraw(1,15)




