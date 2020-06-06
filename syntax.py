# Python Crash Course 2nd Edition
# pylint: disable=invalid-name

# STRINGS AND VARIABLES

print("Hello Python world!")

message = "Hello Word!"
print(message)

# String manipulations
name = "jOHn smItH"
print(name.title())
print(name.upper())
print(name.lower())

# String interpolation
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

# Whitespace: new lines and tabs
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping whitespace
language = 'python '
print(language.rstrip())
print(language)

language = ' python'
print(language.lstrip())
print(language)

# NUMBERS

# Calculations
print(2 + 3*4)
print((2 + 3) * 4)

# Floats
print(1 + 1.5)

# Separating thousands
universe_age = 14_000_000_000
print(universe_age)

# Multiple assignment
x, y, z = 0, 0, 0
print(x)
print(y)
print(z)

# Constants
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

# LISTS


