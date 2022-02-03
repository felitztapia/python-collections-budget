
#from . 
import Expense
import collections
import matplotlib.pyplot as plt

expenses= Expense.Expenses()

expenses.read_expenses('data/spending_data.csv')

spending_Categories=[]

for x in expenses.list :
    spending_Categories.append(x.category)
    
spending_counter = collections.Counter(spending_Categories)

print(spending_counter)

top5 = spending_counter.most_common(5)

print(top5)

categories, count = zip(*top5)

fig, ax = plt.subplots()

ax.bar(categories,count)
ax.set_title('# of Purchases by Category')
plt.show()