#calculate the tip

bill = float(input("Enter the bill: R"))
tip = 0.15 #written in decimal

val_tip = bill * tip
total_cost = bill + val_tip

print(f"here is the tip: {val_tip}")
print(f"here is the tip: {round(val_tip, 2)} rounded")

print(f"here is the total cost: {total_cost}")
print(f"here is the total_cost: {round(total_cost, 2)} rounded")