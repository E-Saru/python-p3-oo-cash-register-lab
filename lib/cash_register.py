#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
      self.items=[]
      self.total=0
      self.discount=discount

  def add_item(self, item_name, price, quantity=1):
      self.items.extend([item_name]*quantity)
      total_price = price * quantity
      if self.discount > 0 and total_price >= self.discount:
        total_price -= (self.discount / 100) * total_price
      self.total += total_price

  def apply_discount(self):
      if self.discount>0:
          discount_amount=int(self.total*((100-self.discount)/100))
          self.total - discount_amount
          print(f"After the discount, the total comes to ${self.total}.")
      else:
          print("There is no discount to apply.")

  def void_last_transaction(self):
      if self.items:
          last_item_price = self.total / len(self.items)
          self.total -= last_item_price
          del self.items[-1]
      else:
          print("There are no transactions to void.")
          