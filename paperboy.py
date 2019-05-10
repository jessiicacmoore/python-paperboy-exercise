class Paperboy:
  def __init__(self, name):
    self.name = name
    self.experience = 0
    self.earnings = 0
    self.quota = 50

  def __str__(self):
    return "Name: {}\nExperience: {}\nEarnings: ${:.2f}\nQuota: {}".format(self.name, self.experience, self.earnings, int(self.quota))

  def increase_quota(self):
    self.quota += self.earnings / 2

  def deliver(self, start_address, end_address):
    papers_delivered = abs(end_address - start_address)
    money_earned = papers_delivered * .25
    self.experience += papers_delivered
    self.earnings += money_earned
    if papers_delivered < self.quota:
      self.increase_quota()
      self.earnings -= 2
      return "You only delivered {} papers, and have been penalized $2.00. You've earned ${:.2f} on this delivery".format(papers_delivered, money_earned - 2)
    self.increase_quota()
    return "Well done! You've delivered {} papers and earned ${:.2f} on this delivery!".format(papers_delivered, money_earned)
  
  def report(self):
    return f"I'm {self.name}, I've delivered {self.experience} papers so far!"


paperboy1 = Paperboy('Johnny')

print(paperboy1)
print(paperboy1.deliver(680, 650))
print(paperboy1.report())
print(paperboy1)
print('-------------------------')
print(paperboy1.deliver(680, 800))
print(paperboy1.report())
print(paperboy1)