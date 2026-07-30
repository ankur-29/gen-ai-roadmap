from products import products, categories

# create a set
categories_set = set(categories)

print("Categories Set:")
print(categories_set)

# 2. Add a new category
categories_set.add("Gaming")
categories_set.add("Electronics")   # Duplicate

print("After Adding Categories:")
print(categories_set)

# 3. Check if category exists
print("Is 'Gaming' Present?", "Gaming" in categories_set)

# Extra
print("Total Unique Categories:", len(categories_set))