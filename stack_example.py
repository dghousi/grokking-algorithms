def greet(name):
    print("Hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("How are you, "+ name + "?")

def bye():
    print("Ok bye")


greet("Ali")