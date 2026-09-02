def most_expensive_product(products):
    '''
    Find the product with the highest price.

    Parameters:
        products (dict): Dictionary of product: price pairs.

    Returns:
        tuple: (product_name, price) of the highest priced product.
    '''
    return max(products.items(), key=lambda x: x[1])



products = {
    "Laptop": 80000,
    "Phone": 60000,
    "Tablet": 35000,
    "Monitor": 15000
}

product, price = most_expensive_product(products)
print(f"The most expensive product is '{product}' with price {price}.")
