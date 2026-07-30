from products import products, categories, price_dict

# 1. Create catalog
catalog = []

for i in range(len(products)):
    catalog.append((products[i], price_dict[products[i]], categories[i]))

print("Catalog:")
print(catalog)

# 2. Create category_to_products dictionary
category_to_products = {}

for product, category in zip(products, categories):
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("\nCategory to Products:")
print(category_to_products)

# 3. Category with maximum products
max_category = max(category_to_products, key=lambda x: len(category_to_products[x]))

print("\nCategory with Maximum Products:", max_category)
print("Products:", category_to_products[max_category])