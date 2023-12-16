#!/usr/bin/env python3
import ipdb

class CashRegister:
  def __init__(self, discount=0 ):
    self.discount = discount
    self.total = 0
    self.items = []
  
  # Properties
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    self._discount = discount

# Methods
  def add_item(self, item, price, quantity = 1):
    [self.items.append(item) for num in range(quantity)]
    self.price = price * quantity
    self.total += self.price
    
  def apply_discount(self):
    if not self.discount:
      print ("There is no discount to apply.")
    else:
      discounted_price = self.total * ((100-self.discount)/100)
      self.total = discounted_price
      print(f"After the discount, the total comes to ${discounted_price:.0f}.")

  def void_last_transaction(self):
    self.total -= self.price




# ipdb.set_trace()