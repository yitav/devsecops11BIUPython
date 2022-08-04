# sol 1:

# Ranges
# The range type represents an immutable sequence of numbers
# and is commonly used for looping a specific number of times in for loops.


# sol 2:

# class range(start, stop[, step])
# The arguments to the range constructor must be integers
# (either built-in int or any object that implements the __index__() special method).
# If the step argument is omitted, it defaults to 1.
# If the start argument is omitted, it defaults to 0. If step is zero, ValueError is raised.
#
# For a positive step, the contents of a range r are determined by the formula
# r[i] = start + step*i where i >= 0 and r[i] < stop.
#
# For a negative step, the contents of the range are still determined by the formula
# r[i] = start + step*i, but the constraints are i >= 0 and r[i] > stop.

# >>> list(range(0, 10, 3))
# [0, 3, 6, 9]
# >>> list(range(0, -10, -1))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]


# sol 3:

# wrap the range Built-in Function with list Built-in Function

# >>> list(range(0))
# []
# >>> list(range(1, 0))
# []


# sol 4:

# The while statement is used for repeated execution as long as an expression is true:
#
# while_stmt ::=  "while" assignment_expression ":" suite
#                 ["else" ":" suite]
# This repeatedly tests the expression and, if it is true, executes the first suite;
# if the expression is false (which may be the first time it is tested) the suite of the else clause,
# if present, is executed and the loop terminates.


# sol 5:

# do-while loops first does the iteration and only then checks for the loop's condition.
# while loop first checks the condition and only then performs the loop's iteration.
# b.t.w there is no do-while native construct in python


# sol 6:

# while True:
#     #loop body
#     if !conditionToContinue :
#         break;


# sol 7:

# A break statement executed in the first suite terminates the loop without executing the else clause’s suite.
# A continue statement executed in the first suite skips the rest of the suite
# and goes back to testing the expression.
