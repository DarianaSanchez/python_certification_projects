def arithmetic_arranger(problems, results=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'

  arranged_problems = ''
  operations = {
    '+': lambda num_1, num_2: str(int(num_1) + int(num_2)),
    '-': lambda num_1, num_2: str(int(num_1) - int(num_2)),
  }

  first_line = []
  second_line = []
  lines_line = []
  results_line = []

  for problem in problems:
    operands = problem.split()
    num_1, operator, num_2 = operands
    max_num = max(len(num_1), len(num_2))
    total_len = max_num + 2  # operation sign(1) + one space(1) = 2

    if operator not in operations:
      return "Error: Operator must be '+' or '-'."
    elif not (num_1.isnumeric() and num_2.isnumeric()):
      return "Error: Numbers must only contain digits."
    elif max_num > 4:
      return "Error: Numbers cannot be more than four digits."

    first_line.append(num_1.rjust(total_len, ' '))
    second_line.append((f"{operator} {num_2.rjust(max_num, ' ')}"))
    lines_line.append('-' * total_len)

    if results:
      result = operations[operator](num_1, num_2)
      results_line.append(result.rjust(total_len, ' '))

    solved_set = (first_line, second_line, lines_line, results_line)
    arranged_problems = '\n'.join(['    '.join(i) for i in solved_set if i])

  return arranged_problems