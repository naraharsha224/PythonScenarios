#Scenario: You have a dataset containing information about products in an inventory. You need to filter out the products that are out of stock.
#Task: Write a Python script using boolean operations to filter out the out-of-stock products from the dataset.

# Sample dataset representing products in inventory
products = [
    {"name": "Laptop", "price": 999, "stock": 10},
    {"name": "Mouse", "price": 20, "stock": 0},
    {"name": "Keyboard", "price": 50, "stock": 5},
    {"name": "Monitor", "price": 200, "stock": 0},
    {"name": "Headphones", "price": 100, "stock": 8}
]

# Initialize an empty list to store outof-stock products
outof_stock_products = []

# Loop through each product in the dataset
for product in products:
    # Check if the product's stock quantity is less than 1
    if product["stock"]<1:
        # If yes, add the product to the list of outof-stock products
        outof_stock_products.append(product)

# Print the filtered products
for product in outof_stock_products:
    print(product)
