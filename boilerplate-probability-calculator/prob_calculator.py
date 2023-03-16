import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = []

    if kwargs:
      for key, value in kwargs.items():
        self.contents.extend([key] * value)

  def draw(self, balls_count):
    if balls_count >= len(self.contents):
      return self.contents

    draw_result = []
    remaining_turns = balls_count

    while remaining_turns > 0:
      draw_num = random.randint(0, len(self.contents) - 1)
      draw_result.append(self.contents.pop(draw_num))
      remaining_turns -= 1 

    return draw_result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  remaining_exprm = num_experiments

  while remaining_exprm > 0:
    hat_copy = copy.deepcopy(hat)
    draw_result = hat_copy.draw(num_balls_drawn)

    if all([draw_result.count(key) >= val for (key, val) in expected_balls.items()]):
      m += 1

    remaining_exprm -= 1 

  return m/num_experiments