from pyscript import display
#Shop Order System (Python Data Types)

#String
shop_name = "PokéMart"
owner_name = "Briana Sy"

#Integer
year_since = 1956

#Float
tax_rate = 0.08

#Boolean
has_delivery = True
is_buy_in = True

#List
product_names = ["Poke Ball", "Great Ball", "Ultra Ball"]
beverages = ["Potion", "Super Potion", "Hyper Potion"]


#Tupple
business_hours = ("1:00 AM", "11:59 PM")

#Dictionary
menu = {
    "Poke Ball" : 200.00,
    "Great Ball" : 600.00,
    "Ultra Ball" : 800.00,
    "Potion" : 200.00,
    "Super Potion" : 700.00,
    "Hyper Potion" : 1500.00,
}

#Set
common_allergens = {"gluten", "dairy"}

#Display Shop Information
display(shop_name, target="name1")
display(f"Established by: {owner_name}", target="owner")
display(f"Since: {year_since}", target="since")
display(f"| Shop Inventory", target="heading2")
display(f"DELIBIRD PRESENTS | Buying", target="heading1")

#Display Shop menu
display(product_names[0], target="prod1")
display(f"₽{menu['Poke Ball']:.2f}", target="price1")

display(product_names[1], target="prod2")
display(f"₽{menu['Great Ball']:.2f}", target="price2")

display(product_names[2], target="prod3")
display(f"₽{menu['Ultra Ball']:.2f}", target="price3")

display(beverages[0], target="prod4")
display(f"₽{menu['Potion']:.2f}", target="price4")

display(beverages[1], target="prod5")
display(f"₽{menu['Super Potion']:.2f}", target="price5")

display(beverages[2], target="prod6")
display(f"₽{menu['Hyper Potion']:.2f}", target="price6")

#Display Additional Information
display(f"Open: {business_hours[0]} - {business_hours[0]}", target="openingHours")

#Display Order Type
display(f"Available to Buy Now", target="orderType")