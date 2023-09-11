import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = list()
    for x in kwargs:
      for i in range(kwargs[x]):
        self.contents.append(x)
        
  def draw(self, num):
    if num <= len(self.contents):
      bolas_retiradas = list()
      for i in range(num):
        elemento = random.choice(self.contents)
        bolas_retiradas.append(elemento)
        self.contents.remove(elemento)
      return bolas_retiradas
    else:
      return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  eureka = 0
  for i in range(num_experiments):
    copy_hat = copy.deepcopy(hat)
    bolas_obtenidas = copy_hat.draw(num_balls_drawn)
    for key, value in expected_balls.items():
      if bolas_obtenidas.count(key) < value:
        break
    else:
      eureka += 1
  return eureka/num_experiments

