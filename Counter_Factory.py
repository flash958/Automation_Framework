def create_counter(start=0):
    count=[start]
    def counter():
        count[0]+=1
        return count
    return counter


CounterA = create_counter()
CounterB= create_counter()
print(CounterA())
print(CounterA())
print(CounterB())
print(CounterA())

