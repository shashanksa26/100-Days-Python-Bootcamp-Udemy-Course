name=input("What  is your name? \n")
location=input("Where are you from? ")
def greet(name,location):
    print(f"Hello there {name}!!")
    print(f"How you are doing?")
    print(f"Isn't the weather nice there in {location}?")
greet(name,location)
greet(location=12,name=34)
greet("ronit","somewhere")