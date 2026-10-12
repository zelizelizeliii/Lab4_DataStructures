
# ADDITIONAL EXERCISE 1
# Engineering Test Data Organizer

from collections import Counter, defaultdict

LAST_NAME = "Gabilan"
SEED_NUM = 6
FAVORITE_ARTIST = "The 1975"

sources = [f"{LAST_NAME}_T{i}" for i in range(1, 6)]
categories = [
    "TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"
]

# Generate records using the artist's character positions
records = []

for i, source in enumerate(sources):
    for j, category in enumerate(categories):
        char_value = ord(FAVORITE_ARTIST[(i + j) % len(FAVORITE_ARTIST)])
        value = SEED_NUM + (char_value % 20) + i + j

        records.append({
            "source": source,
            "category": category,
            "value": value
        })

# Add a repeated source/category record
records.append(records[0].copy())

# Add extra measurements under existing categories
records.append({
    "source": sources[0],
    "category": "TEMPERATURE",
    "value": SEED_NUM + 30
})

print("=== GENERATED TEST DATA ===")
for record in records:
    print(record)

# Organize records by source and category
organized = defaultdict(list)

for record in records:
    organized[record["source"]].append(record)

print("\n=== ORGANIZED TEST DATA ===")
for source, measurements in organized.items():
    print(source, measurements)

# Identify repeated source/category pairs
pair_counts = Counter(
    (r["source"], r["category"]) for r in records
)

repeated = {
    pair: count for pair, count in pair_counts.items()
    if count > 1
}

distinct_pairs = set(pair_counts.keys())

print("\n=== REPEATED / DISTINCT DATA ===")
print("Repeated Source/Category Pairs:", repeated)
print("Distinct Source/Category Pairs:", len(distinct_pairs))

# Numerical summaries by category
category_values = defaultdict(list)

for record in records:
    category_values[record["category"]].append(record["value"])

print("\n=== NUMERICAL SUMMARIES ===")
for category, values in sorted(category_values.items()):
    print(
        category,
        "Count:", len(values),
        "Minimum:", min(values),
        "Maximum:", max(values),
        "Average:", round(sum(values) / len(values), 2)
    )

print("\n=== ORDERED RESULTS ===")
ordered_records = sorted(
    records,
    key=lambda r: (r["source"], r["category"], r["value"])
)

for record in ordered_records:
    print(record)

print("\n=== FINAL SUMMARY ===")
print("Total Records:", len(records))
print("Distinct Sources:", len(sources))
print("Measurement Categories:", len(categories))
print("Repeated Pairs:", repeated)
print("Dataset successfully organized and analyzed.")