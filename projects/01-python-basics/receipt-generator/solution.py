shop_name = input("Enter shop name: ").strip()
item_count = int(input("How many different items are you buying? "))

items = []
subtotal = 0.0

for _ in range(item_count):
    name = input("Enter item name: ").strip()
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    line_total = quantity * unit_price
    subtotal += line_total

    items.append((name, quantity, unit_price, line_total))

tax = subtotal * 0.05
grand_total = subtotal + tax

print("=" * 40)
print(f"{shop_name:^40}")
print("=" * 40)

for name, quantity, unit_price, line_total in items:
    print(f"{name:<15} x{quantity:<3} @ {unit_price:>6.2f} = {line_total:>7.2f}")

print("-" * 40)
print(f"Subtotal: {subtotal:>25.2f}")
print(f"Tax (5%): {tax:>25.2f}")
print(f"GRAND TOTAL: {grand_total:>22.2f}")
print("=" * 40)
FIRST