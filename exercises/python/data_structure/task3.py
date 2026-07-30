from products import price_dict

#Add new product
price_dict["Speaker"] = 3000

# Update existing product price
price_dict["Mouse"] = 900

# Remove product
product = "Keyboard"

if product in price_dict:
    del price_dict[product]
else:
    print("Product not found.")

# 3. Average price
total = sum(price_dict.values())
average = total / len(price_dict)

print("Average Price:", average)

# Extra
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most Expensive:", max_product, "-", price_dict[max_product])
print("Least Expensive:", min_product, "-", price_dict[min_product])