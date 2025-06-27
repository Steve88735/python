actual_cost=float(input("Enter the actual cost of the item: "))
sale_amount=float(input("Enter the sale amount of the item: "))
if (sale_amount> actual_cost):
    amount=sale_amount - actual_cost
    print("Profit amount is:", amount)
else:
    amount=actual_cost - sale_amount
    print("Loss amount is:",amount)