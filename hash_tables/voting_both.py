
voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote!")

check_voter("Muhammad")
check_voter("Jane")
check_voter("Ali")
check_voter("Jane")

print(voted)