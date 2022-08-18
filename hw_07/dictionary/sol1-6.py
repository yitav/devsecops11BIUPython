
# sol 1:

# Another useful data type built into Python is the dictionary (see Mapping Types — dict).
# Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”.
# Unlike sequences, which are indexed by a range of numbers,
# dictionaries are indexed by keys,
# which can be any immutable type; strings and numbers can always be keys.
# Tuples can be used as keys if they contain only strings, numbers, or tuples;
# if a tuple contains any mutable object either directly or indirectly,
# it cannot be used as a key. You can’t use lists as keys,
# since lists can be modified in place using index assignments,
# slice assignments, or methods like append() and extend().

# It is best to think of a dictionary as a set of key: value pairs,
# with the requirement that the keys are unique (within one dictionary).
# A pair of braces creates an empty dictionary: {}.
# Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary;
# this is also the way dictionaries are written on output.

# one should use a dictionary when it is right according to correct programming principles -
# such as runtime , dry, clean code and so on.


# sol 2:

# keys can be any immutable object
# values have no restriction


# sol 3:

# JSON Syntax Rules
# JSON syntax is derived from JavaScript object notation syntax:
#
# Data is in name/value pairs
# Data is separated by commas
# Curly braces hold objects
# Square brackets hold arrays

# The JSON format is almost identical to JavaScript objects.
#
# In JSON, keys must be strings, written with double quotes:

# JSON Values
# In JSON, values must be one of the following data types:
#
# a string
# a number
# an object
# an array
# a boolean
# null
# In JavaScript values can be all of the above, plus any other valid JavaScript expression, including:
#
# a function
# a date
# undefined

# from the above explanation one can see that json is not python dictionary nor xml.


# sol 4:

# creation :

# In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’.
# or Dictionary can also be created by the built-in function dict().
# An empty dictionary can be created by just placing to curly braces{}.
# Dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value.
# Values in a dictionary can be of any data type and can be duplicated,
# whereas keys can’t be repeated and must be immutable.

# adding and override:

# Addition of elements can be done in multiple ways.
# One value at a time can be added to a Dictionary by defining value along with the key e.g. Dict[Key] = ‘Value’.
# Updating an existing value in a Dictionary can be done by using the built-in update() method.
# Nested key values can also be added to an existing Dictionary.
#
# Note- While adding a value,
# if the key-value already exists,
# the value gets updated otherwise a new Key with the value is added to the Dictionary.

# delete

# Method 1: Remove a Key from a Dictionary using the del
# The del keyword can be used to in-place delete the key that is present in the dictionary in Python.
# One drawback that can be thought of using this is that it raises an exception
# if the key is not found and hence non-existence of the key has to be handled.
# Demonstrating key-value pair deletion using del.

# Method 2: Remove a Key from a Dictionary using pop()
# The pop() can be used to delete a key and its value inplace.
# The advantage over using del
# is that it provides the mechanism to print desired value if tried to remove a non-existing dict. pair.
# Second, it also returns the value of the key that is being removed
# in addition to performing a simple delete operation.


# sol 5:

# dictionary_name.keys()


# sol 6:

# dictionary_name.values()
