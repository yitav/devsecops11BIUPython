# sol1:

# 4.8.4. Arbitrary Argument Lists
# Finally, the least frequently used option is to specify that a function
# can be called with an arbitrary number of arguments.
# These arguments will be wrapped up in a tuple (see Tuples and Sequences).
# Before the variable number of arguments, zero or more normal arguments may occur.

# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))

# Normally, these variadic arguments will be last in the list of formal parameters,
# because they scoop up all remaining input arguments that are passed to the function.
# Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments,
# meaning that they can only be used as keywords rather than positional arguments.

# 4.8.5. Unpacking Argument Lists
# The reverse situation occurs when the arguments are already in a list or tuple
# but need to be unpacked for a function call requiring separate positional arguments.
# For instance, the built-in range() function expects separate start and stop arguments.
# If they are not available separately,
# write the function call with the *-operator to unpack the arguments out of a list or tuple:
#
# >>>
# >>> list(range(3, 6))            # normal call with separate arguments
# [3, 4, 5]
# >>> args = [3, 6]
# >>> list(range(*args))            # call with arguments unpacked from a list
# [3, 4, 5]
# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:


# sol 2:

# Tuples are immutable,
# and usually contain a heterogeneous sequence of elements that are accessed via unpacking
# (see later in this section) or indexing (or even by attribute in the case of namedtuples).


# sol 3:

# OOP (Object-oriented programming) is a programming paradigm based on the concept of "objects",
# which can contain data and code: data in the form of fields (often known as attributes or properties),
# and code, in the form of procedures (often known as methods).
#
# A common feature of objects is that procedures (or methods)
# are attached to them and can access and modify the object's data fields


# sol 4:

# A class is a blueprint which you use to create objects.
# An object is an instance of a class - it's a concrete 'thing' that you made using a specific class.


# sol 5:

# 9.3.1. Class Definition Syntax
# The simplest form of class definition looks like this:
#
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# The Unified Modeling Language (UML) is a general-purpose, developmental, modeling language
# in the field of software engineering that is intended to provide a standard way
# to visualize the design of a system.

# sol 6:

# constructor


# sol 7:

# A function is a piece of code that is called by name.
# It can be passed data to operate on (i.e. the parameters) and can optionally return data (the return value).
# All data that is passed to a function is explicitly passed.
#
# A method is a piece of code that is called by a name that is associated with an object.
# In most respects it is identical to a function except for two key differences:
#
# A method is implicitly passed the object on which it was called.
# A method is able to operate on data that is contained within the class
# (remembering that an object is an instance of a class - the class is the definition,
# the object is an instance of that data).
