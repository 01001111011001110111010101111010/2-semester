#skaber variabel
types_of_people = 10

#skaber variablen x som er en formateret string (dvs. der kan komme andre variabler ind i den)
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#printer x og y variablerne, dvs. ikke alle de andre variabler
print(x)
print(y)

#printer x og y variablerne, men nu som formaterede strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# flere variabler
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#printer variablerne, dog bliver hilarious formateret med .format
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)