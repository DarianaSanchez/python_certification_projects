class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=''):
    new_deposit = {
      'amount': amount,
      'description': description
    }
    self.ledger.append(new_deposit)

  def withdraw(self, amount, description=''):
    sufficient_funds = self.check_funds(amount)
  
    if sufficient_funds:
      new_withdrawal = {
        'amount': amount * -1,
        'description': description
      }
      self.ledger.append(new_withdrawal)
      return True

    return False

  def get_balance(self):
    return sum([x['amount'] for x in self.ledger])

  def get_withdrawals_total(self):
    return sum([x['amount'] for x in self.ledger if x['amount'] < 0])

  def transfer(self, amount, category):
    completed = self.withdraw(amount, f'Transfer to {category.name}')

    if completed:
      category.deposit(amount, f'Transfer from {self.name}')
      return True

    return False

  def check_funds(self, amount):
    balance = self.get_balance()
    return balance >= amount

  def __str__(self):
    budget_status = []

    def align(desc, amt):
      return '{}{}{}'.format(desc, ' ' * (30 - len(desc + amt)), amt)

    for trans in self.ledger:
      aligned = align(
        trans['description'][:23],
        '{:.2f}'.format(trans['amount'])
      )
      budget_status.append(aligned)

    asterisk_count = (30 - len(self.name)) // 2
    budget_status.insert(0, f"{'*' * asterisk_count}{self.name.title()}{'*' * asterisk_count}")

    budget_status.append(f"Total: {'{:.2f}'.format(self.get_balance())}")

    return '\n'.join(budget_status)

def create_spend_chart(categories):
  tab = ' ' * 4
  chart = ['Percentage spent by category']
  percents = reversed(range(0, 101, 10))
  category_percents = []
  categ_names = [categ.name for categ in categories]
  withdraw_total = sum([categ.get_withdrawals_total() for categ in categories])

  for cat in categories:
    rounded = abs(cat.get_withdrawals_total() / withdraw_total) * 100
    category_percents.append((round(rounded)/10)*10)

  for percent in percents:
    categ_applies = map(lambda x: x >= percent, category_percents)
    line = f"{str(percent).rjust(3, ' ')}| {'  '.join([(c and 'o') or ' ' for c in categ_applies])}  "
    chart.append(line)

  chart.append(f"{tab}{'-' * ((len(categories) * 3) + 1)}")

  for name_line in range(len(max(categ_names, key=len))):
    line = f'{tab} '

    for c in categ_names:
      if len(c) > name_line:
        line += f'{c[name_line]}  '
      else:
        line += (' ' * 3)

    chart.append(line)

  return '\n'.join(chart)