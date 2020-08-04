# Variable explaining lovely loveseat.
lovely_loveseat_description = "Lovely Loveseat, Tufted polyester blend on wood. 32 inches high * 40 inches wide * 30 inches deep. Red or white."
# Variable defining lovely loveseat price.
lovely_loveseat_price = 254.00
#variable explaining stylish settee.
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high * 54.75 inches wide * 28 inches deep. Black."
#variable defining stylish settee price.
stylish_settee_price = 180.50
#variable explaining luxurious lamp.
luxurious_lamp_description = " Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
#variable defining luxurious lamp price.
luxurious_lamp_price = 52.15
#variable to calculate sales tax.
sales_tax = .088
customer_one_total = 0
#variable to keep track of total expenses.
customer_one_total += lovely_loveseat_price + luxurious_lamp_price
#variable on items customers have bought.
customer_one_itemization = ""
#adding to a variable.
customer_one_itemization += lovely_loveseat_description + luxurious_lamp_description
#variable to calculate customer tax.
customer_one_tax = customer_one_total * sales_tax
#add variables customer_one_total and customer_one_tax together.
customer_one_total + customer_one_tax
#prints customer one items.
print("Customer One Items:")
#prints variable customer_one_itemization
print(customer_one_itemization)
#prints customer one total:
print("Customer One Total:")
print(customer_one_total)