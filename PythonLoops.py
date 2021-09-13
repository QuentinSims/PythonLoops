hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# working out total price of hair cuts
total_price = 0
for price in prices:
  total_price += price

# working out the average price of hair cuts
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

# making a new list of prices of hair cuts - 5
new_prices = [price - 5 for price in prices]
print(new_prices)

# printing out total revenur
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7

# advertising hair cuts less than 30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)
