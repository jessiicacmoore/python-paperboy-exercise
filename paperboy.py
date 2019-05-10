class Paperboy:
  def __init__(self, name, experience, earnings):
    self.name = name
    self.experience = experience
    self.earnings = earnings

  def __str__(self):
    return "Name: {}\nExperience: {}\nEarnings: ${:.2f}".format(self.name, self.experience, self.earnings)

paperboy1 = Paperboy('Johnny', 50, 12.50)