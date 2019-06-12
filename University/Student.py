class Students:

  def __init__(self,saxeli,gvari,wlovaneba,sashualo):
    self.saxeli = saxeli
    self.gvari = gvari
    self.wlovaneba = wlovaneba
    self.sashualo = sashualo
  def core(self):
    if self.sashualo < 92:
      print("B Qula [{}]".format(self.sashualo))
    else:
      print("A Qula [{}]".format(self.sashualo))

s1 = Students("nikusha","razmadze","18",50)
s2 = Students("giorgi","shevardnadze","25",95)

s1.core()
s2.core()