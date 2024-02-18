def do_something():
    print("I did something!")

do_something()

def do_more_things(a, b):
    print("A IS", a, "B IS", b)

do_more_things("hello", 1)

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

def halløj():
    print("Jamen halløj til dig")

def halløj_to(halløjsa1, halløjsa2):
    print(f"halløjsa1: {halløjsa1}, halløjsa2: {halløjsa2}")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
halløj()
halløj_to("hej", "hallo")