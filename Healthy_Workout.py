

def healthy_work(func):
    def wrapper(*args):
        result=func(*args)
        if(result<500):
            print("This workout is not intense enough")
        else:
            print("Workout is intense")
    return wrapper

@healthy_work
def calories_burnt(duratiopn_of_workout,calories_burnt_per_min):
    return duratiopn_of_workout*calories_burnt_per_min

calories_burnt(30,10)
