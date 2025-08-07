main = input("how many main courses do you want? ")
dessert = input("how many desserts do you want? ")
drinks = input("how many drinks do you want? ")
main = float(main)
main_price = 12.5 * main
dessert = float(dessert)
dessert_price = 6.0 * dessert
drinks = float(drinks)
drinks_price = 3.55 * drinks
drinks_price = float(drinks_price)
main_price = float(main_price)
dessert_price = float(dessert_price)
total = drinks_price + main_price + dessert_price
print("the total price is", total)