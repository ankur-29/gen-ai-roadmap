from products import products, sample_product

# Print the 2nd and last product
print("Second Product:", products[1])
print("Last Product:", products[-1])

# 4. Append two new products
products.append("Webcam")
products.append("Printer")

print("Updated Product List:")
print(products)

# Extra Optional
product_list = list(sample_product)
product_list[1] = 60000
sample_product = tuple(product_list)

print("Updated Tuple:")
print(sample_product)