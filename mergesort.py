from time import sleep

def print_items(list):
    for item in list:
        print(item)

print(print_items([55,1,1,3,5,56]))

def print_items2(list):
    for item in list:
        sleep(1) 
        print('<sleep> ' + str(item))

print(print_items2([55,1,1,3,5,56]))