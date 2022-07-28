#The syntax of a loop represented in the context free grammar in the bnf is presented below:

# 8.2. The while statement
# The while statement is used for repeated execution as long as an expression is true:
#
# while_stmt ::=  "while" assignment_expression ":" suite
#                 ["else" ":" suite]
# This repeatedly tests the expression and, if it is true, executes the first suite; if the expression is false (which may be the first time it is tested) the suite of the else clause, if present, is executed and the loop terminates.
#
# A break statement executed in the first suite terminates the loop without executing the else clause’s suite. A continue statement executed in the first suite skips the rest of the suite and goes back to testing the expression.
#
# 8.3. The for statement
# The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object:
#
# for_stmt ::=  "for" target_list "in" expression_list ":" suite
#               ["else" ":" suite]
# The expression list is evaluated once; it should yield an iterable object. An iterator is created for the result of the expression_list. The suite is then executed once for each item provided by the iterator, in the order returned by the iterator. Each item in turn is assigned to the target list using the standard rules for assignments (see Assignment statements), and then the suite is executed. When the items are exhausted (which is immediately when the sequence is empty or an iterator raises a StopIteration exception), the suite in the else clause, if present, is executed, and the loop terminates.
#
# A break statement executed in the first suite terminates the loop without executing the else clause’s suite. A continue statement executed in the first suite skips the rest of the suite and continues with the next item, or with the else clause if there is no next item.
#
# The for-loop makes assignments to the variables in the target list. This overwrites all previous assignments to those variables including those made in the suite of the for-loop:
#
# for i in range(10):
#     print(i)
#     i = 5             # this will not affect the for-loop
#                       # because i will be overwritten with the next
#                       # index in the range
# Names in the target list are not deleted when the loop is finished, but if the sequence is empty, they will not have been assigned to at all by the loop. Hint: the built-in function range() returns an iterator of integers suitable to emulate the effect of Pascal’s for i := a to b do; e.g., list(range(3)) returns the list [0, 1, 2].


#examples:

# 4.2. for Statements
# The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):
#
# >>>
# >>> # Measure some strings:
# ... words = ['cat', 'window', 'defenestrate']
# >>> for w in words:
# ...     print(w, len(w))
# ...
# cat 3
# window 6
# defenestrate 12
# Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:
#
# # Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
#
# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#
# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status