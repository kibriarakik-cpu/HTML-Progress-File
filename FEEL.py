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

# MY TRAVEL TICKET COUNTER
# ================================
 
# PART 1 - TYPES OF DATA
 
passenger_name = "Messi"        # str - text
destination = "New Jersey"      # str - text
ticket_price = 850.50           # float - decimal number
number_of_tickets = 3           # int - whole number
is_available = True             # bool - True or False
 
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: $", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)
 
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))
 
# PART 2 - ARITHMETIC OPERATORS
 
total_cost = ticket_price * number_of_tickets
discount = 100
final_cost = total_cost - discount
 
print("\nTotal Cost: $", total_cost)
print("Discount: $", discount)
print("Final Cost: $", final_cost)
 
print("Double Ticket Price: $", ticket_price * 2)
print("Ticket Price After $50 Increase: $", ticket_price + 50)
print("Half Ticket Price: $", ticket_price / 2)
 
# PART 3 - COMPARISON OPERATORS
 
print("\nIs ticket price under $1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", number_of_tickets > 2)
print("Is destination New Jersey?", destination == "New Jersey")
print("Is final cost more than $2000?", final_cost > 2000)
 
# PART 4 - STRING OPERATIONS
 
travel_message = passenger_name + " is travelling to " + destination + "."
print("\nTravel Message:", travel_message)
 
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))
 
# PART 5 - SWAPPING VALUES
 
morning_ticket_price = 700
evening_ticket_price = 900
 
print("\nBefore Swapping:")
print("Morning Ticket Price: $", morning_ticket_price)
print("Evening Ticket Price: $", evening_ticket_price)
 
morning_ticket_price, evening_ticket_price = evening_ticket_price, morning_ticket_price
 
print("\nAfter Swapping:")
print("Morning Ticket Price: $", morning_ticket_price)
print("Evening Ticket Price: $", evening_ticket_price)
 
# FINAL SUMMARY
 
print("\n================================")
print("TRAVEL TICKET SUMMARY")
print("================================")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: $", final_cost)
print("Booking Confirmed?", is_available)
