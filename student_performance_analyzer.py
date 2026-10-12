
# ADDITIONAL EXERCISE 2
# Student Performance Data Analyzer

from collections import Counter, defaultdict

LAST_NAME = "Gabilan"
SEED_NUM = 6
FAVORITE_ARTIST = "The 1975"

students = [f"{LAST_NAME}_S{i}" for i in range(1, 6)]
subjects = [
    "PROGRAMMING", "MATHEMATICS", "ELECTRONICS",
    "PHYSICS", "ENGLISH"
]

def get_category(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Satisfactory"
    elif score >= 60:
        return "Needs Improvement"
    return "Failing"

# Generate student-subject records
records = []

for i, student in enumerate(students):
    for j, subject in enumerate(subjects):
        char_value = ord(
            FAVORITE_ARTIST[(i + j) % len(FAVORITE_ARTIST)]
        )
        score = 50 + ((SEED_NUM * (i + 1) + char_value + j) % 51)

        records.append({
            "student": student,
            "subject": subject,
            "score": score
        })

# Add one repeated student-subject record
records.append(records[0].copy())

# Add one incomplete record
records.append({
    "student": students[0],
    "subject": "PROGRAMMING",
    "score": None
})

print("=== GENERATED PERFORMANCE RECORDS ===")
for record in records:
    print(record)

# Identify duplicates and incomplete records
record_counts = Counter(
    (r["student"], r["subject"])
    for r in records
)

repeated = {
    pair: count for pair, count in record_counts.items()
    if count > 1
}

incomplete = [r for r in records if r["score"] is None]
valid_records = [r for r in records if r["score"] is not None]

print("\n=== REPEATED / INCOMPLETE RECORDS ===")
print("Repeated Student-Subject Pairs:", repeated)
print("Incomplete Records:", incomplete)

# Categorize valid scores
for record in valid_records:
    record["category"] = get_category(record["score"])

print("\n=== PERFORMANCE CATEGORIES ===")
for record in valid_records:
    print(record)

# Summaries by student and subject
student_scores = defaultdict(list)
subject_scores = defaultdict(list)

for record in valid_records:
    student_scores[record["student"]].append(record["score"])
    subject_scores[record["subject"]].append(record["score"])

print("\n=== STUDENT SUMMARIES ===")
for student, scores in sorted(student_scores.items()):
    print(
        student,
        "Count:", len(scores),
        "Average:", round(sum(scores) / len(scores), 2)
    )

print("\n=== SUBJECT SUMMARIES ===")
for subject, scores in sorted(subject_scores.items()):
    print(
        subject,
        "Count:", len(scores),
        "Average:", round(sum(scores) / len(scores), 2)
    )

print("\n=== ORDERED RESULTS ===")
for record in sorted(
    valid_records,
    key=lambda r: (r["student"], r["subject"])
):
    print(record)

print("\n=== FINAL STUDENT PERFORMANCE REPORT ===")
print("Total Generated Records:", len(records))
print("Valid Score Records:", len(valid_records))
print("Incomplete Records:", len(incomplete))
print("Repeated Student-Subject Pairs:", repeated)
print("Student Count:", len(students))
print("Subject Count:", len(subjects))
print("Performance analysis completed.")