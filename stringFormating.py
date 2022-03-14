# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
# OUT: Numbers: 4 5 6
# cada argumento da função format é colocado na string na posição correspondente
# a posição é determinada por {}

print("{0}{1}{0}".format("abra", "cad"))

a = "{x}, {y}".format(x=5, y=12)
print(a)
b = "{f}, {g}".format(f=2, g=8)
print(b)

# join - is a list of string with another string as a separator
print(", ".join(["spam", "eggs", "ham"]))
# out: spam, eggs, ham

# replace - replaces one substring in a string with another
print("Hello ME".replace("ME", "world!"))
# out: Hello world!

# startswith and endswith - determine if there is a substring at the start and end of a string, respectively
print("This is a sentence".startswith("This"))
# out: True

print("This is a sentence".endswith("sentence"))
# out: True

# lower and upper - changes the case of a string
print("This is a sentence.".upper())
# out: "THIS IS A SENTENCE"
print("AN ALL CAPS SENTENCE".lower())
# out: "an all caps sentence"

# split - the oposite of join, turns a string with a certain separator into a list
print("spam, eggs, ham".split(", "))
# out: ['spam', 'eggs', 'ham']