# sol 1 :

# input is a built-in function
# input([prompt])
# If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:
#
# >>>
# >>> s = input('--> ')
# --> Monty Python's Flying Circus
# >>> s
# "Monty Python's Flying Circus"
# If the readline module was loaded, then input() will use it to provide elaborate line editing and history features.
#
# Raises an auditing event builtins.input with argument prompt before reading input
#
# Raises an auditing event builtins.input/result with the result after successfully reading input.

# sol 2 :

# wrap the input function with the int or float class's constructor
# int(input())
# float(input())

# sol 3 :

# str.split(sep=None, maxsplit=- 1)
# Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
#
# If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].
#
# For example:
#
# >>>
# >>> '1,2,3'.split(',')
# ['1', '2', '3']
# >>> '1,2,3'.split(',', maxsplit=1)
# ['1', '2,3']
# >>> '1,2,,3,'.split(',')
# ['1', '2', '', '3', '']
# If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].
#
# For example:
#
# >>>
# >>> '1 2 3'.split()
# ['1', '2', '3']
# >>> '1 2 3'.split(maxsplit=1)
# ['1', '2 3']
# >>> '   1   2   3   '.split()
# ['1', '2', '3']

# sol 4 :

# str.format(*args, **kwargs)
# Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
#
# >>>
# "The sum of 1 + 2 is {0}".format(1+2)
# 'The sum of 1 + 2 is 3'

# This function saves string concatenation in the number of arguments

# sol 5 :

# 6.10.2. Membership test operations
# The operators in and not in test for membership. x in s evaluates to True if x is a member of s, and False otherwise. x not in s returns the negation of x in s. All built-in sequences and set types support this as well as dictionary, for which in tests whether the dictionary has a given key. For container types such as list, tuple, set, frozenset, dict, or collections.deque, the expression x in y is equivalent to any(x is e or x == e for e in y)


# sol 6 :

# the language's statement's context free grammar in BNF

# compound_stmt ::=  if_stmt
#                    | while_stmt
#                    | for_stmt
#                    | try_stmt
#                    | with_stmt
#                    | match_stmt
#                    | funcdef
#                    | classdef
#                    | async_with_stmt
#                    | async_for_stmt
#                    | async_funcdef
# suite         ::=  stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
# statement     ::=  stmt_list NEWLINE | compound_stmt
# stmt_list     ::=  simple_stmt (";" simple_stmt)* [";"]

#assignment_expression ::=  [identifier ":="] expression

# 8.1. The if statement
# The if statement is used for conditional execution:
#
# if_stmt ::=  "if" assignment_expression ":" suite
#              ("elif" assignment_expression ":" suite)*
#              ["else" ":" suite]
# It selects exactly one of the suites by evaluating the expressions one by one until one is found to be true (see section Boolean operations for the definition of true and false); then that suite is executed (and no other part of the if statement is executed or evaluated). If all expressions are false, the suite of the else clause, if present, is executed.

# 4.1. if Statements
# Perhaps the most well-known statement type is the if statement. For example:
#
# >>>
# >>> x = int(input("Please enter an integer: "))
# Please enter an integer: 42
# >>> if x < 0:
# ...     x = 0
# ...     print('Negative changed to zero')
# ... elif x == 0:
# ...     print('Zero')
# ... elif x == 1:
# ...     print('Single')
# ... else:
# ...     print('More')
# ...
# More
# There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation. An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.


# sol 7 :

# as you can see from the previous answer - the language interpreter parses the if statement by the indentation


