print("------Shopping Bill Generator------")
items=[]
prices=[]
quantities=[]
n=int(input("Enter number of items you want to buy:"))
for i in range(n):
  print(f"\nItem {i+1}")
  name= input("Enter item name:")
  price=float(input("Enter price of the item:"))
  qty=int(input("Enter quantity:"))
  items.append(name)
  prices.append(price)
  quantities.append(qty)
total=0
for i in range(n):
  total+= prices[i]*quantities[i]
print("\n------ Final Bill ------")
for i in range(n):
  print(f"{items[i]} X {quantities[i]} = Rs{prices[i]*quantities[i]}")
print("\nTotal Amount to Pay: Rs", total)
print("--------------------------------------")
    
