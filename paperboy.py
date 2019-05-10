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
    self.experience += papers_delivered

    if papers_delivered < self.quota:
      self.earnings -= 2

      for paper in range(papers_delivered):
        self.earnings += 0.25 
      self.increase_quota()      
      return "You only delivered {} papers, and have been penalized $2.00.".format(papers_delivered)
      
    elif papers_delivered >= self.quota:
      for paper in range(papers_delivered):
        self.earnings += 0.25 
      for paper in range(papers_delivered - self.quota):
        self.earnings += 0.25 
      self.increase_quota() 
      return "Well done! You've delivered {} papers!".format(papers_delivered)     

  def report(self):
    return f"I'm {self.name}, I've delivered {self.experience} papers so far!"


paperboy1 = Paperboy('Johnny')

print(paperboy1)
print('-------------------------')
print(paperboy1.deliver(680, 600))
print(paperboy1.report())
print(paperboy1)
print('-------------------------')
print(paperboy1.deliver(680, 670))
print(paperboy1.report())
print(paperboy1)