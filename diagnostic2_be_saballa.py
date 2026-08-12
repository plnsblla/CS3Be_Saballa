def calculate_total(topping_count):
    total = topping_count*1.50+10
    return total

print("--- Welcome to the PSHSWVCIC Co-op Pizza Parlor! ---")
print()
print("Plain cheese pizza costs 10.00; any additional toppings cost 1.50 each. Available additional toppings include 'pepperoni' 'mushrooms' 'extra cheese'")
print("Please type 'done' when finished.")
topping_count = 0
topping = str(input("Enter desired toppings: "))
while topping != "done":
    if topping == "pepperoni":
        topping_count = topping_count+1
        topping = str(input("Enter desired toppings: "))
    elif topping == "mushrooms":
            topping_count = topping_count+1
            topping = str(input("Enter desired toppings: "))
    elif topping == "extra cheese":
            topping_count = topping_count+1
            topping = str(input("Enter desired toppings: "))
    else:
         print("Not in the menu. Please try again:")
         topping = str(input("Enter desired toppings: "))

if topping == "done":
        total = calculate_total(topping_count)
        discount_code = str(input("Do you have a discount code? If not, enter 'No': "))
        if discount_code == "PYTHON20":
            total = total*0.80
            print()
            print("You received a 20 percent discount!")
            print("Your total bill is: ", total)
        else:
            print("Your total bill is: ", total)

print("Thank you for ordering!")
