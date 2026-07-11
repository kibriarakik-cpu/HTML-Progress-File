a = input("Enter your name: ")
grade = input("Enter your grade: ")
print("Hello, " + a + "! You are in grade " + grade + ". Welcome to vscode!")
print("Welcome to the world of programming!")
print(4)
print("Hello, \nWorld!")
print("All keywords of python are below:")
help("keywords")
help("modules")
help("symbols")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(len(letters)):
    print(letters[i])
Sauce = input("Enter your favorite sauce: ")
print("Your favorite sauce is " + Sauce + ".")
Sports = input("Enter your favorite sport: ")
print("Your favorite sport is " + Sports + ".")
Jobs = input("Enter your dream job: ")
print("Your dream job is " + Jobs + ".")
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
