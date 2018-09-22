#initialize the variable 
types_of_people = 10

#use format string and initialize a new variable
x = f"There are {types_of_people} types of people."

#these strings initialize the binary and do_not variable, the y variable concatinates with a format #string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#This takes two of the same data types and adds them together
print(w + e)