def grill():
    print("Food is Grilled")


def fry():
    print("Food is fried")

def boil():
    print("Food is Boiled")

print("Before Seasoning")

grill()
fry()
boil()

def seasoning(chef):
    def wrapper():
        print("Adding Seasoning to make the food tasty")
        chef()
        print("Food is properly garnished")
    return wrapper

@seasoning
def grill():
    print("Food is Grilled")

@seasoning
def fry():
    print("Food is fried")

@seasoning
def boil():
    print("Food is Boiled")

print("After seasoning")
grill()
fry()
boil()



