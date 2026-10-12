
# ADDITIONAL EXERCISE 3
# Transaction History Analyzer

from collections import Counter, defaultdict

LAST_NAME = "Gabilan"
SEED_NUM = 6
FAVORITE_ARTIST = "The 1975"

customers = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]

prices = {
    "NOTEBOOK": 50.00,
    "PEN": 15.00,
    "USB": 250.00,
    "HEADPHONES": 500.00,
    "CALCULATOR": 300.00
}

products = list(prices.keys())
transactions = []

# Generate transactions using student-specific inputs
for i, customer in enumerate(customers):
    for j, product in enumerate(products):
        char_value = ord(
            FAVORITE_ARTIST[(i + j) % len(FAVORITE_ARTIST)]
        )

        quantity = 1 + (
            (SEED_NUM + char_value + i + j) % 5
        )

        transactions.append({
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "price": prices[product]
        })

# Add one repeated customer-product transaction
transactions.append(transactions[0].copy())

# Calculate transaction values
for transaction in transactions:
    transaction["total"] = round(
        transaction["quantity"] * transaction["price"], 2
    )

print("=== GENERATED TRANSACTION RECORDS ===")
for transaction in transactions:
    print(transaction)

# Identify repeated customer-product combinations
pair_counts = Counter(
    (t["customer"], t["product"]) for t in transactions
)

repeated = {
    pair: count for pair, count in pair_counts.items()
    if count > 1
}

print("\n=== REPEATED / DISTINCT TRANSACTIONS ===")
print("Repeated Customer-Product Pairs:", repeated)
print("Distinct Customers:", len(set(t["customer"] for t in transactions)))
print("Distinct Products:", len(set(t["product"] for t in transactions)))

# Summarize transactions by customer and product
customer_totals = defaultdict(float)
product_totals = defaultdict(float)
product_quantities = defaultdict(int)

for transaction in transactions:
    customer_totals[transaction["customer"]] += transaction["total"]
    product_totals[transaction["product"]] += transaction["total"]
    product_quantities[transaction["product"]] += transaction["quantity"]

print("\n=== CUSTOMER SUMMARIES ===")
for customer, total in sorted(customer_totals.items()):
    print(customer, "Total Purchases:", round(total, 2))

print("\n=== PRODUCT SUMMARIES ===")
for product in sorted(product_totals):
    print(
        product,
        "Quantity Sold:", product_quantities[product],
        "Total Sales:", round(product_totals[product], 2)
    )

# Sort all transactions
ordered_transactions = sorted(
    transactions,
    key=lambda t: (t["customer"], t["product"])
)

print("\n=== ORDERED RESULTS ===")
for transaction in ordered_transactions:
    print(transaction)

overall_total = sum(t["total"] for t in transactions)

print("\n=== FINAL CONSOLIDATED TRANSACTION REPORT ===")
print("Total Transaction Records:", len(transactions))
print("Distinct Customers:", len(customers))
print("Distinct Products:", len(products))
print("Repeated Customer-Product Pairs:", repeated)
print("Overall Transaction Value:", round(overall_total, 2))
print("Transaction analysis completed.")