import random
import csv

electronics = [
    "Apple iPhone 15", "Apple iPhone 15 Pro", "Apple iPhone 12"
]

fashion = [
    "Adidas Sports T-Shirt", "Men Cotton Shirt"
]

groceries = [
    "Wheat Flour 1kg","Milk 1L"
]

tot_prods = electronics + fashion + groceries

def generate_products(n=500):
    products = []
    for i in range(1, n + 1):
        name = random.choice(tot_prods)
        products.append((i, name))
    return products

if __name__ == "__main__":
    products = generate_products()

    with open("products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["product_id", "product_name"])
        writer.writerows(products)

    print("products.csv created")
