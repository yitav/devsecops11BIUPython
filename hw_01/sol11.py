equation = input("please enter your equation:")

equation_list = equation.split()

equation_to_calculate = equation_list[:-2]
equation_right_side = float(equation_list[-1])

equation_left_side = "".join(equation_to_calculate)
equation_result_calculated = eval(equation_left_side)

print(equation_result_calculated == equation_right_side)
