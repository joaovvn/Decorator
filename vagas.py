class Texto:
  
  def __init__(self, texto):
    self._texto = texto

  def print(self):
    return self._texto

class Design(Texto):

  def __init__(self, design):
    self._design = design

  def print(self):
    return(f'================================================\n{self._design.print()}\n================================================')

class Negrito(Texto):
  def __init__(self, negrito):
    self._negrito = negrito

  def print(self):
    return "\033[1m{}".format(self._negrito.print())