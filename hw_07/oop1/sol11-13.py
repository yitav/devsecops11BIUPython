
# sol 11:


# 9.3.5. Class and Instance Variables
# Generally speaking, instance variables are for data unique to each instance
# and class variables are for attributes and methods shared by all instances of the class:
#
# class Dog:
#
#     kind = 'canine'         # class variable shared by all instances
#
#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance
#
# >>> d = Dog('Fido')
# >>> e = Dog('Buddy')
# >>> d.kind                  # shared by all dogs
# 'canine'
# >>> e.kind                  # shared by all dogs
# 'canine'
# >>> d.name                  # unique to d
# 'Fido'
# >>> e.name                  # unique to e
# 'Buddy'

# part 2 :

# yes it can be deleted with the del keyword


# sol 12:

# constructor


# sol 13:

# The __str__ method is what gets called happens when you print it,
# and the __repr__ method is what happens when you use the repr() function
# (or when you look at it with the interactive prompt).
#
# If no __str__ method is given, Python will print the result of __repr__ instead.
# If you define __str__ but not __repr__, Python will use what you see above as the __repr__,
# but still use __str__ for printing.
