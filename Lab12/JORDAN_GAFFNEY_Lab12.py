import pandas as pd

revenue = pd.Series([1000, 900, 1100, 400, 2000], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], dtype=int,
name='revenue')
print(revenue)
expenses = pd.Series([900, 900, 900, 900, 900], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], dtype=int, name='expenses')
print(expenses)
print(revenue['Wed'])
print(expenses[1:4])

netprofit = (revenue-expenses)
average = netprofit.mean()
print(average)