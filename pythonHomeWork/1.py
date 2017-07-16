def remove_duplicates(string):
   new_string = "".join(sorted(set(string)))
   if new_string:
     return (new_string, len(string)-len(new_string))
   else:
     return "Please provide only alphabets"

def length(lists):
a = 0
answer = ''
for item in lists:
    x = len(item)
    if x > a:
        a = x
        answer = item
    elif x == a:
        if item not in list:
            answer = answer + ' ' + item
return answer
print length(list)

def longest(string):
	return max(string.split(), key=len)


def my_sort(numbers):
    odd  = [n for n in numbers if n % 2 != 0]
    even = [n for n in numbers if n % 2 == 0]
    return sorted(odd) + sorted(even)

def power(x, y):
  if y == 0:
    return 1
  else:
    return x*power(x, y-1)

  

def is_isogram(word):
    if not isinstance(word, str):
        raise TypeError('Argument should be a string')
    if not word or (word.strip() == ""):
        isogram = False
    else:
        isogram = len(word) == len(set(word.lower()))
    return word, isogram



# Create a class called ShoppingCart.

# Create a constructor that has no arguments and sets the total attribute to zero, and initializes an empty dict attribute named items.

# Create a method add_item that requires item_name, quantity and price arguments. This method should add the cost of the added items to the current value of total. It should also add an entry to the items dict such that the key is the item_name and the value is the quantity of the item.

# Create a method remove_item that requires similar arguments as add_item. It should remove items that have been added to the shopping cart and are not required. This method should deduct the cost of these items from the current total and also update the items dict accordingly. If the quantity of items to be removed exceeds current quantity in cart, assume that all entries of that item are to be removed.

# Create a method checkout that takes in cash_paid and returns the value of balance from the payment. If cash_paid is not enough to cover the total, return Cash paid not enough.

# Create a class called Shop that has a constructor which initializes an attribute called quantity at 100.

# Make sure Shop inherits from ShoppingCart.

# In the Shop class, override the remove_item method, such that calling Shop's remove_item with no arguments decrements quantity by one.
class ShoppingCart(object):
  
  def __init__(self):
    self.total = 0
    self.items = {}
    
  def add_item(self, item_name, quantity, price):
    self.total += quantity * price
    if type(item_name) == str and quantity > 0:
        self.items.update({item_name: quantity})
        
  def remove_item(self, item_name, quantity, price):
    if quantity >= self.items[item_name] and quantity >= 1:
        items_cost = price * self.items[item_name]
        self.total -= items_cost
        del self.items[item_name]
    else:
        self.total -= quantity * price
        self.items[item_name] -= quantity
        
  def checkout(self, cash_paid):
    balance = 0
    if cash_paid < self.total:
        return "Cash paid not enough"
    balance = cash_paid - self.total
    return balance


class Shop(ShoppingCart):
  def __init__(self):
      self.quantity = 100
      
  def remove_item(self):
      self.quantity -= 1



