snack_name   = "Chips"    # str   — text
price        = 1.50       # float — decimal
quantity     = 10         # int   — whole number
is_available = True       # bool  — True or False

print(type(snack_name))   # <class 'str'>
print(type(price))        # <class 'float'>

price    = 1.50
quantity = 10
total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 0.25)
print("Double stock:", quantity * 2)
total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 0.25)
print("Double stock:", quantity * 2)

print("Is price under 2$?", price < 2 )
print("Is quantity greater than 5?", quantity > 5 )
print("Is price equal to 1.50?", price == 1.50 )
shop_name = "Quick" + " " + "Bites"
print("Shop name:", shop_name)
print("Letters in snack name:", len(snack_name))
print("First letter:", snack_name[0])

price_a = 1.50
price_b = 3.00

temp    = price_a   # Step 1: save price_a
price_a = price_b   # Step 2: move price_b into price_a
price_b = temp      # Step 3: put saved value into price_b

print("After swap:", price_a, "and", price_b)
