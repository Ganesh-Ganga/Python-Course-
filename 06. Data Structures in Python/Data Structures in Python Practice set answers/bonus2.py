# Question:
# Given a dictionary of products and their prices, find the product with the highest price.

# Question:
# Given a dictionary of products and their prices, find the product with the highest price.

products = {
    "Laptop": 75000,
    "Phone": 50000,
    "Tablet": 30000,
    "Monitor": 20000
}

highest_product = ""
highest_price = 0

for product in products:
    if products[product] > highest_price:
        highest_price = products[product]
        highest_product = product

print("Products:", products)
print("Product with highest price:", highest_product)
print("Price:", highest_price)
